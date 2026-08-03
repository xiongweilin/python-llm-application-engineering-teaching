[CmdletBinding()]
param(
    [ValidateRange(1, 65535)]
    [int]$Port = 8766,
    [switch]$NoBrowser,
    [switch]$Quiet
)

$ErrorActionPreference = 'Stop'
$courseRoot = Split-Path -Parent $PSScriptRoot
$indexPath = Join-Path $courseRoot 'index.html'
$serverScript = Join-Path $PSScriptRoot 'course_server.py'
$stateDirectory = Join-Path $env:LOCALAPPDATA 'Ratio\PythonLLMEngineeringCourse'
$statePath = Join-Path $stateDirectory "server-$Port.json"
$urlPath = Join-Path $stateDirectory "launch-$Port.url"
$baseUrl = "http://127.0.0.1:$Port/index.html"
$startedProcess = $null

function Show-CourseError([string]$Message) {
    if (-not $Quiet) {
        $shell = New-Object -ComObject WScript.Shell
        $null = $shell.Popup($Message, 0, 'Python 与 LLM 应用工程', 16)
    }
}

function Get-ListenerProcessId {
    $connections = @(Get-NetTCPConnection -LocalAddress '127.0.0.1' -LocalPort $Port -State Listen -ErrorAction SilentlyContinue)
    $ids = @($connections | Select-Object -ExpandProperty OwningProcess -Unique)
    if ($ids.Count -gt 1) { throw "端口 $Port 存在多个监听进程。" }
    if ($ids.Count -eq 1) { return [int]$ids[0] }
    return $null
}

function Get-HttpIndexHash {
    $response = Invoke-WebRequest -Uri $baseUrl -UseBasicParsing -TimeoutSec 2
    if ([int]$response.StatusCode -ne 200) { throw "课程首页返回 HTTP $([int]$response.StatusCode)。" }
    $bytes = [Text.Encoding]::UTF8.GetBytes($response.Content)
    return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes))
}

try {
    if (-not (Test-Path -LiteralPath $indexPath) -or -not (Test-Path -LiteralPath $serverScript)) {
        throw '课程首页或本地服务器脚本不存在。'
    }
    New-Item -ItemType Directory -Path $stateDirectory -Force | Out-Null
    $expectedHash = (Get-FileHash -LiteralPath $indexPath -Algorithm SHA256).Hash
    $serverProcessId = Get-ListenerProcessId
    $token = $null

    if ($null -ne $serverProcessId) {
        if ((Get-HttpIndexHash) -ne $expectedHash) {
            throw "端口 $Port 已被其他内容占用。"
        }
        $processInfo = Get-CimInstance Win32_Process -Filter "ProcessId=$serverProcessId"
        if ($processInfo.Name -notin @('python.exe', 'pythonw.exe') -or [string]$processInfo.CommandLine -notmatch 'course_server\.py') {
            throw "端口 $Port 不是本课程服务器。"
        }
        if (-not (Test-Path -LiteralPath $statePath)) {
            throw '课程服务器状态文件缺失，请先运行关闭器再重新打开。'
        }
        $state = Get-Content -LiteralPath $statePath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ([int]$state.ProcessId -ne $serverProcessId) {
            throw '课程服务器状态与监听进程不一致。'
        }
        $token = [string]$state.Token
    }
    else {
        Remove-Item -LiteralPath $statePath, $urlPath -Force -ErrorAction SilentlyContinue
        $pythonResult = @(& python -c 'import sys; print(sys.executable)')
        if ($LASTEXITCODE -ne 0 -or $pythonResult.Count -eq 0) { throw '未找到可用的 Python。' }
        $pythonExe = [string]$pythonResult[0]
        $pythonwExe = Join-Path (Split-Path -Parent $pythonExe) 'pythonw.exe'
        if (-not (Test-Path -LiteralPath $pythonwExe)) { throw "未找到无窗口启动器：$pythonwExe" }

        $token = [guid]::NewGuid().ToString('N')
        $quotedScript = '"' + $serverScript.Replace('"', '\"') + '"'
        $quotedState = '"' + $statePath.Replace('"', '\"') + '"'
        $quotedUrl = '"' + $urlPath.Replace('"', '\"') + '"'
        $arguments = @($quotedScript, '--port', [string]$Port, '--token', $token, '--state-file', $quotedState, '--url-file', $quotedUrl)
        $startedProcess = Start-Process -FilePath $pythonwExe -ArgumentList $arguments -WindowStyle Hidden -PassThru
        $serverProcessId = $startedProcess.Id

        $ready = $false
        foreach ($attempt in 1..24) {
            Start-Sleep -Milliseconds 250
            try {
                if ((Get-HttpIndexHash) -eq $expectedHash) { $ready = $true; break }
            }
            catch {
                if ($startedProcess.HasExited) { break }
            }
        }
        if (-not $ready) { throw '课程服务器未能在 6 秒内提供当前首页。' }

        [pscustomobject]@{
            ProcessId = $serverProcessId
            Port = $Port
            Root = $courseRoot
            Token = $token
            RecordedAt = (Get-Date).ToString('o')
        } | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding UTF8
    }

    $version = (Get-Item -LiteralPath $indexPath).LastWriteTimeUtc.Ticks
    $launchUrl = "${baseUrl}?v=$version&token=$token"
    Set-Content -LiteralPath $urlPath -Value $launchUrl -Encoding UTF8

    if (-not $NoBrowser) {
        $startInfo = [Diagnostics.ProcessStartInfo]::new()
        $startInfo.FileName = $launchUrl
        $startInfo.UseShellExecute = $true
        [Diagnostics.Process]::Start($startInfo) | Out-Null
    }
}
catch {
    if ($null -ne $startedProcess -and -not $startedProcess.HasExited) {
        Stop-Process -Id $startedProcess.Id -Force -ErrorAction SilentlyContinue
    }
    Remove-Item -LiteralPath $statePath, $urlPath -Force -ErrorAction SilentlyContinue
    Show-CourseError $_.Exception.Message
    exit 1
}

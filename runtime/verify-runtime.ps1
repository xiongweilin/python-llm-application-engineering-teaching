[CmdletBinding()]
param(
    [ValidateRange(1, 65534)]
    [int]$LauncherPort = 8878,
    [ValidateRange(2, 65535)]
    [int]$ShutdownPort = 8879
)

$ErrorActionPreference = 'Stop'
$courseRoot = Split-Path -Parent $PSScriptRoot
$openScript = Join-Path $PSScriptRoot 'open-course.ps1'
$closeScript = Join-Path $PSScriptRoot 'close-course.ps1'
$serverScript = Join-Path $PSScriptRoot 'course_server.py'
$indexPath = Join-Path $courseRoot 'index.html'
$temporaryDirectory = Join-Path $env:TEMP 'ratio-course-runtime-verification'
$testStatePath = Join-Path $temporaryDirectory 'server.json'
$testUrlPath = Join-Path $temporaryDirectory 'launch.url'

function Get-ListenerCount([int]$Port) {
    return @(Get-NetTCPConnection -LocalAddress '127.0.0.1' -LocalPort $Port -State Listen -ErrorAction SilentlyContinue).Count
}

function Get-IndexHash([int]$Port) {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:$Port/index.html" -UseBasicParsing -TimeoutSec 2
    $bytes = [Text.Encoding]::UTF8.GetBytes($response.Content)
    return [pscustomobject]@{
        Status = [int]$response.StatusCode
        Hash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes))
        CacheControl = [string]$response.Headers['Cache-Control']
    }
}

if ($LauncherPort -eq $ShutdownPort) { throw '两个测试端口不能相同。' }
if ((Get-ListenerCount $LauncherPort) -ne 0 -or (Get-ListenerCount $ShutdownPort) -ne 0) {
    throw '测试端口已被占用。'
}

$expectedHash = (Get-FileHash -LiteralPath $indexPath -Algorithm SHA256).Hash
$launcherResult = $null
$shutdownResult = $null
$directProcess = $null

try {
    & pwsh -NoProfile -NonInteractive -File $openScript -Port $LauncherPort -NoBrowser -Quiet
    if ($LASTEXITCODE -ne 0) { throw "启动器退出码为 $LASTEXITCODE。" }
    $served = Get-IndexHash $LauncherPort
    $theme = Invoke-WebRequest -Uri "http://127.0.0.1:$LauncherPort/assets/course.css" -UseBasicParsing -TimeoutSec 2
    $markdown = Invoke-WebRequest -Uri "http://127.0.0.1:$LauncherPort/SESSION-PAGE-CONTRACT.md" -UseBasicParsing -TimeoutSec 2
    $launcherResult = [pscustomobject]@{
        HttpStatus = $served.Status
        HashMatches = ($served.Hash -eq $expectedHash)
        CacheControl = $served.CacheControl
        ListenerCount = Get-ListenerCount $LauncherPort
        ThemeStatus = [int]$theme.StatusCode
        ThemeContentType = [string]$theme.Headers['Content-Type']
        ThemeMarkerPresent = $theme.Content.Contains('--course-accent')
        MarkdownStatus = [int]$markdown.StatusCode
        MarkdownContentType = [string]$markdown.Headers['Content-Type']
        MarkdownChinesePresent = $markdown.Content.Contains('正式学习会话页面契约')
    }
    & pwsh -NoProfile -NonInteractive -File $closeScript -Port $LauncherPort -Quiet
    if ($LASTEXITCODE -ne 0 -or (Get-ListenerCount $LauncherPort) -ne 0) {
        throw '关闭器没有完整停止测试服务。'
    }

    New-Item -ItemType Directory -Path $temporaryDirectory -Force | Out-Null
    Remove-Item -LiteralPath $testStatePath, $testUrlPath -Force -ErrorAction SilentlyContinue
    $pythonPath = [string]@(& python -c 'import sys; print(sys.executable)')[0]
    if ($LASTEXITCODE -ne 0 -or -not $pythonPath) { throw '未找到 Python。' }
    $pythonwPath = Join-Path (Split-Path -Parent $pythonPath) 'pythonw.exe'
    $arguments = @(
        '"' + $serverScript + '"',
        '--port', [string]$ShutdownPort,
        '--token', 'verification-token',
        '--state-file', '"' + $testStatePath + '"',
        '--url-file', '"' + $testUrlPath + '"'
    )
    $directProcess = Start-Process -FilePath $pythonwPath -ArgumentList $arguments -WindowStyle Hidden -PassThru

    $ready = $false
    foreach ($attempt in 1..20) {
        Start-Sleep -Milliseconds 200
        try {
            if ((Get-IndexHash $ShutdownPort).Status -eq 200) { $ready = $true; break }
        }
        catch {
            if ($directProcess.HasExited) { break }
        }
    }
    if (-not $ready) { throw '关闭接口测试服务未就绪。' }

    $wrong = Invoke-WebRequest -Uri "http://127.0.0.1:$ShutdownPort/__course__/shutdown?token=wrong" -Method Post -SkipHttpErrorCheck -UseBasicParsing -TimeoutSec 2
    $listenerAfterWrongToken = Get-ListenerCount $ShutdownPort
    $right = Invoke-WebRequest -Uri "http://127.0.0.1:$ShutdownPort/__course__/shutdown?token=verification-token" -Method Post -UseBasicParsing -TimeoutSec 2
    $null = $directProcess.WaitForExit(5000)
    $shutdownResult = [pscustomobject]@{
        WrongTokenStatus = [int]$wrong.StatusCode
        ListenerAfterWrongToken = $listenerAfterWrongToken
        CorrectTokenStatus = [int]$right.StatusCode
        ProcessExited = $directProcess.HasExited
        ListenerAfterCorrectToken = Get-ListenerCount $ShutdownPort
    }

    $passed = (
        $launcherResult.HttpStatus -eq 200 -and
        $launcherResult.HashMatches -and
        $launcherResult.CacheControl -eq 'no-store' -and
        $launcherResult.ListenerCount -eq 1 -and
        $launcherResult.ThemeStatus -eq 200 -and
        $launcherResult.ThemeContentType -match 'text/css' -and
        $launcherResult.ThemeMarkerPresent -and
        $launcherResult.MarkdownStatus -eq 200 -and
        $launcherResult.MarkdownContentType -match 'text/markdown;\s*charset=utf-8' -and
        $launcherResult.MarkdownChinesePresent -and
        $shutdownResult.WrongTokenStatus -eq 403 -and
        $shutdownResult.ListenerAfterWrongToken -eq 1 -and
        $shutdownResult.CorrectTokenStatus -eq 200 -and
        $shutdownResult.ProcessExited -and
        $shutdownResult.ListenerAfterCorrectToken -eq 0
    )

    [pscustomobject]@{
        Passed = $passed
        Launcher = $launcherResult
        ShutdownEndpoint = $shutdownResult
    } | ConvertTo-Json -Depth 4
    if (-not $passed) { exit 1 }
}
finally {
    if ((Get-ListenerCount $LauncherPort) -ne 0) {
        & pwsh -NoProfile -NonInteractive -File $closeScript -Port $LauncherPort -Quiet
    }
    if ($null -ne $directProcess -and -not $directProcess.HasExited) {
        Stop-Process -Id $directProcess.Id -Force -ErrorAction SilentlyContinue
    }
    Remove-Item -LiteralPath $testStatePath, $testUrlPath -Force -ErrorAction SilentlyContinue
}

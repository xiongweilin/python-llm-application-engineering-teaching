[CmdletBinding()]
param(
    [ValidateRange(1, 65535)]
    [int]$Port = 8765,
    [switch]$Quiet
)

$ErrorActionPreference = 'Stop'
$courseRoot = Split-Path -Parent $PSScriptRoot
$indexPath = Join-Path $courseRoot 'index.html'
$stateDirectory = Join-Path $env:LOCALAPPDATA 'Ratio\PythonLLMEngineeringCourse'
$statePath = Join-Path $stateDirectory "server-$Port.json"
$urlPath = Join-Path $stateDirectory "launch-$Port.url"
$baseUrl = "http://127.0.0.1:$Port/index.html"

function Show-CourseError([string]$Message) {
    if (-not $Quiet) {
        $shell = New-Object -ComObject WScript.Shell
        $null = $shell.Popup($Message, 0, 'Python 与 LLM 应用工程', 16)
    }
}

try {
    $connections = @(Get-NetTCPConnection -LocalAddress '127.0.0.1' -LocalPort $Port -State Listen -ErrorAction SilentlyContinue)
    $ids = @($connections | Select-Object -ExpandProperty OwningProcess -Unique)
    if ($ids.Count -eq 0) {
        Remove-Item -LiteralPath $statePath, $urlPath -Force -ErrorAction SilentlyContinue
        exit 0
    }
    if ($ids.Count -ne 1) { throw "端口 $Port 存在多个监听进程。" }

    $serverProcessId = [int]$ids[0]
    $processInfo = Get-CimInstance Win32_Process -Filter "ProcessId=$serverProcessId"
    if ($processInfo.Name -notin @('python.exe', 'pythonw.exe') -or [string]$processInfo.CommandLine -notmatch 'course_server\.py') {
        throw "端口 $Port 不是本课程服务器；没有停止该进程。"
    }

    $expectedHash = (Get-FileHash -LiteralPath $indexPath -Algorithm SHA256).Hash
    $response = Invoke-WebRequest -Uri $baseUrl -UseBasicParsing -TimeoutSec 2
    $bytes = [Text.Encoding]::UTF8.GetBytes($response.Content)
    $actualHash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes))
    if ($actualHash -ne $expectedHash) { throw '当前服务返回的不是本课程首页。' }

    Stop-Process -Id $serverProcessId -Force
    foreach ($attempt in 1..20) {
        Start-Sleep -Milliseconds 100
        if (@(Get-NetTCPConnection -LocalAddress '127.0.0.1' -LocalPort $Port -State Listen -ErrorAction SilentlyContinue).Count -eq 0) { break }
    }
    if (@(Get-NetTCPConnection -LocalAddress '127.0.0.1' -LocalPort $Port -State Listen -ErrorAction SilentlyContinue).Count -ne 0) {
        throw "端口 $Port 仍在监听。"
    }
    Remove-Item -LiteralPath $statePath, $urlPath -Force -ErrorAction SilentlyContinue
}
catch {
    Show-CourseError $_.Exception.Message
    exit 1
}

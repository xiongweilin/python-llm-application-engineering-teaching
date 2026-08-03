[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$ShortcutPath = (Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\Python 与 LLM 应用工程.lnk'),
    [string]$BackupDirectory = (Join-Path $env:LOCALAPPDATA 'Ratio\PythonLLMEngineeringCourse\shortcut-backups'),
    [switch]$Quiet
)

$ErrorActionPreference = 'Stop'
$courseRoot = Split-Path -Parent $PSScriptRoot
$launcherPath = Join-Path $PSScriptRoot '打开课程.vbs'
$wscriptPath = Join-Path $env:WINDIR 'System32\wscript.exe'
$description = '打开 Python、LLM 应用与 Agent 工程课程'
$iconLocation = (Join-Path $env:WINDIR 'System32\imageres.dll') + ',74'
$arguments = '"' + $launcherPath + '"'
$shortcutDirectory = Split-Path -Parent $ShortcutPath

foreach ($requiredPath in @($launcherPath, $wscriptPath)) {
    if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
        throw "快捷方式依赖不存在：$requiredPath"
    }
}

$shell = New-Object -ComObject WScript.Shell
$changed = $true
$backupPath = $null

if (Test-Path -LiteralPath $ShortcutPath -PathType Leaf) {
    $current = $shell.CreateShortcut($ShortcutPath)
    $changed = @(
        $current.TargetPath -ne $wscriptPath
        $current.Arguments -ne $arguments
        $current.WorkingDirectory -ne $courseRoot
        $current.Description -ne $description
        $current.IconLocation -ne $iconLocation
    ) -contains $true
}

if (-not $changed) {
    if (-not $Quiet) {
        [pscustomobject]@{ Changed = $false; Shortcut = $ShortcutPath; Backup = $null }
    }
    return
}

if (-not $PSCmdlet.ShouldProcess($ShortcutPath, '创建或更新课程开始菜单快捷方式')) {
    return
}

New-Item -ItemType Directory -Path $shortcutDirectory -Force | Out-Null
if (Test-Path -LiteralPath $ShortcutPath -PathType Leaf) {
    New-Item -ItemType Directory -Path $BackupDirectory -Force | Out-Null
    $backupName = 'Python 与 LLM 应用工程-{0}-{1}.lnk' -f (Get-Date -Format 'yyyyMMdd-HHmmss'), ([guid]::NewGuid().ToString('N').Substring(0, 8))
    $backupPath = Join-Path $BackupDirectory $backupName
    Copy-Item -LiteralPath $ShortcutPath -Destination $backupPath -ErrorAction Stop
}

$temporaryPath = Join-Path $shortcutDirectory ('Python 与 LLM 应用工程-{0}.tmp.lnk' -f [guid]::NewGuid().ToString('N'))
try {
    $candidate = $shell.CreateShortcut($temporaryPath)
    $candidate.TargetPath = $wscriptPath
    $candidate.Arguments = $arguments
    $candidate.WorkingDirectory = $courseRoot
    $candidate.Description = $description
    $candidate.IconLocation = $iconLocation
    $candidate.WindowStyle = 1
    $candidate.Save()

    $saved = $shell.CreateShortcut($temporaryPath)
    if ($saved.TargetPath -ne $wscriptPath -or $saved.Arguments -ne $arguments -or $saved.WorkingDirectory -ne $courseRoot) {
        throw '候选快捷方式校验失败；原入口未替换。'
    }

    Move-Item -LiteralPath $temporaryPath -Destination $ShortcutPath -Force
}
finally {
    Remove-Item -LiteralPath $temporaryPath -Force -ErrorAction SilentlyContinue
}

if (-not $Quiet) {
    [pscustomobject]@{ Changed = $true; Shortcut = $ShortcutPath; Backup = $backupPath }
}

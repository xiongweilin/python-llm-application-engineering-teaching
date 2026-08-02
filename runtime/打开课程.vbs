Option Explicit

Dim shell, fileSystem, scriptDirectory, command, exitCode
Set shell = CreateObject("WScript.Shell")
Set fileSystem = CreateObject("Scripting.FileSystemObject")
scriptDirectory = fileSystem.GetParentFolderName(WScript.ScriptFullName)
command = "pwsh.exe -NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File """ _
    & scriptDirectory & "\open-course.ps1"""
exitCode = shell.Run(command, 0, True)
WScript.Quit exitCode

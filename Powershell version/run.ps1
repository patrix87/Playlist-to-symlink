$TargetFolder = "C:\Music\"
$SourceFile = ".\NoVGM.txt"

# Launch as admin
If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")) {
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" $PSCommandArgs" -Verb RunAs
    Exit
}

#Find the location of the current invocation of main.ps1, remove the filename, set the working directory to that path.
Write-ScriptMsg "Setting Script Directory as Working Directory..."
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path -Path $scriptpath
$dir = Resolve-Path -Path $dir
$null = Set-Location -Path $dir
Write-ScriptMsg "Working Directory : $(Get-Location)"

$playlist = Get-Content -Path $SourceFile
foreach($line in $playlist) {
    $line = $line.trim()
    New-Item -ItemType SymbolicLink -Path "$TargetFolder\$line" -Target $line
}
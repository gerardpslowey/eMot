Write-Host "Installing Docker Desktop 2.1.0.5"

#choco install docker-desktop

Write-Host "Downloading..."
$exePath = "$env:TEMP\Docker-Desktop-Installer.exe"
(New-Object Net.WebClient).DownloadFile('https://desktop.docker.com/win/stable/amd64/Docker%20Desktop%20Installer.exe', $exePath)

Write-Host "Installing..."
cmd /c start /wait $exePath install --quiet
del $exePath

Write-Host "Docker Desktop installed" -ForegroundColor Green
$files = @(
    "index.html",
    "今日计划.html",
    "减脂训练日跟练_三分化.html",
    "减脂完整教程_饮食运动作息动作库.html",
    "减脂全面计划.html",
    "每周小结.html",
    "视频管理后台.html",
    "data.js",
    "shared.js",
    "gist-storage.js",
    "serviceWorker.js",
    "shared.css",
    "manifest.json",
    "icon-192.png",
    "icon-512.png",
    "减脂App软件说明书.md",
    "项目完整文档.md"
)

$zipPath = "减脂App_完整项目_v10.zip"

if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)

foreach ($file in $files) {
    if (Test-Path $file) {
        $entryName = Split-Path $file -Leaf
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $file, $entryName)
        Write-Host "Added: $entryName"
    } else {
        Write-Host "Missing: $file"
    }
}

$zip.Dispose()
Write-Host "`nCreated: $zipPath"

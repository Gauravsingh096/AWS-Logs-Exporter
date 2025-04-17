# CONFIG
$logPrefix = "aws-logs"
$retentionDays = 7

# 1. Download Latest Logs
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$localLog = "$logPrefix-$timestamp.txt"

Write-Host "📥 Downloading logs..." -ForegroundColor Cyan
aws logs filter-log-events `
  --log-group-name /aws/lambda/ConvertLogsToCSV `
  --query 'events[].message' > $localLog

# 2. Show Results
$localPath = Resolve-Path $localLog
Write-Host "`n✅ Logs Saved To:" -ForegroundColor Green
Write-Host "LOCAL: $localPath"

# 3. Open Folder
explorer .

# 4. Cleanup Old Logs
Get-ChildItem "$logPrefix-*.txt" | 
  Where { $_.LastWriteTime -lt (Get-Date).AddDays(-$retentionDays) } | 
  Remove-Item -Force

Write-Host "`n🧹 Cleared logs older than $retentionDays days" -ForegroundColor Yellow

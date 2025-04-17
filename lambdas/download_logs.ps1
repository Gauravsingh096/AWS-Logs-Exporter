# Download Lambda logs with timestamp
$date = Get-Date -Format "yyyyMMdd_HHmm"
$logFile = "lambda_logs_$date.txt"

# Fetch logs
aws logs filter-log-events `
  --log-group-name /aws/lambda/ConvertLogsToCSV `
  --query 'events[].message' > $logFile

# Verify and show output
if (Test-Path $logFile) {
    $lineCount = (Get-Content $logFile).Count
    Write-Host "✅ Saved $lineCount log entries to:" -ForegroundColor Green
    Write-Host (Resolve-Path $logFile) -ForegroundColor Cyan
    explorer .
} else {
    Write-Host "❌ Failed to save logs" -ForegroundColor Red
}

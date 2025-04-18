��# AWS Lambda Log Manager

## Features
- One-command log downloads
- Automatic 7-day retention
- Local timestamped files
- Error handling and validation

## Usage
powershell
# Basic usage
.\manage_logs.ps1

# Custom settings
.\manage_logs.ps1 -LogGroup "/aws/lambda/OtherFunction" -RetentionDays 30 `

Requirements
AWS CLI configured

PowerShell 5.1+

Log files
aws-logs-*.txt

AWS credentials
*.aws/credentials


### 4. `setup.ps1` (Optional Initialization)
powershell
<#
.SYNOPSIS
Environment setup script
#>

# Verify AWS CLI
if (-not (Get-Command aws -ErrorAction SilentlyContinue){
    throw "AWS CLI not found. Install from: https://aws.amazon.com/cli/"
}

# Set execution policy (Windows only)
if ($PSVersionTable.Platform -eq "Win32NT") {
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
}

Write-Host "✅ Environment ready" -ForegroundColor Green

aws-lambda-log-manager/
├── manage_logs.ps1    # Main script
├── README.md          # Documentation
├── .gitignore         # Ignore logs/credentials
└── setup.ps1          # Bootstrap script (optional)

Key Features:
Parameterized Input - Customize via command-line args

Error Handling - Graceful failure with colored output

Clean Architecture - Regions for easy maintenance

Safety Checks - File validation before operations

Documentation - Embedded help and README

To use:

Clone repo

Run .\setup.ps1 (if needed)

## Execute .\manage_logs.ps1



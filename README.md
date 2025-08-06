# 🛡️ Daily Hacker News Headlines Email Automation

This project automates scraping the top 10 headlines from The Hacker News and sends them to your Gmail inbox every day at **9am Malaysia time** using **GitHub Actions**.

---

## 📦 Features

- Scrapes top 10 cybersecurity headlines
- Sends formatted HTML email via Gmail
- Runs daily using GitHub Actions (free tier)
- Secure credentials via GitHub Secrets

---

## 🚀 Setup Instructions

### 1. Clone or Fork This Repo

```bash
git clone https://github.com/your-username/daily-hackernews-email.git


2. Add Secrets to GitHub
Go to your repo → Settings → Secrets and variables → Actions → Add:

Name	Value
GMAIL_USER	Your Gmail address
GMAIL_APP_PASSWORD	Gmail App Password (not your login password)
🔐 Generate App Password at https://myaccount.google.com/apppasswords (2FA must be enabled)

3. Python Script
File: send_hackernews.py

Scrapes headlines and sends email using Gmail SMTP.

4. GitHub Actions Workflow
File: .github/workflows/daily_email.yml

Runs the script daily at 9am Malaysia time (UTC+8).
on:
  schedule:
    - cron: '0 1 * * *'
  workflow_dispatch:


🧪 Manual Test
To test manually:

Go to Actions tab
Select Daily Hacker News Email
Click Run workflow
🛠️ Troubleshooting
No headlines in email: Check scraping logic or site structure
SMTPAuthenticationError: Check Gmail App Password and 2FA
Secrets exposed: Never hardcode credentials in code
🔒 Security Note
You can keep this repo public if:

Secrets are stored securely in GitHub Secrets
No credentials are hardcoded in the script
If unsure, set the repo to private.

📧 Result
You’ll receive an email like:
Subject: Top 10 Headlines from The Hacker News
Body: List of clickable headlines


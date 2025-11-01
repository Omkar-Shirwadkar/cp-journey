In Powershell:
echo "| $(Get-Date -Format 'yyyy-MM-dd') | not less than a and not more than b |" >> README.md
git add README.md
git commit -m "JIRA_ID | log_$(Get-Date -Format 'yyyy-MM-dd')"
git push


In GitBash, WSL:
echo "| $(date +%Y-%m-%d) | Using README to track changes |" >> README.md
git add README.md
git commit -m "JIRA_ID | log_$(date +%Y-%m-%d)"
git push

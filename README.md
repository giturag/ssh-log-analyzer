# Linux SSH Log Analyzer

A Python-based tool that analyzes Linux authentication logs
to detect suspicious login activity such as brute-force attempts.

## Features:
- Detect failed login attempts
- Identify successful logins
- Flag suspicious IPs with repeated failures
- Works with /var/log/auth.log format

Technologies:
Python
Regex
Linux authentication logs

## How to run
Examples
`python log_analyzer.py /var/log/auth.log`

`python3 log_analyzer.py sample_auth.log`

## Output Example
Failed Login Attempts by IP
---------------------------
192.168.1.45 : 7
192.168.1.50 : 2

Successful Logins by IP
---------------------------
192.168.1.20 : 1

Suspicious IPs
---------------------------
ALERT: 192.168.1.45 has 7 failed login attempts
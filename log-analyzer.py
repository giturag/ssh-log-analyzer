import re
import sys
from collections import defaultdict

# Check if user passed a log file
if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <logfile>")

log_file = sys.argv[1]

failed_attempts = defaultdict(int)
successful_logins = defaultdict(int)

# Regex pattern for IP addresses, 
failed_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\+\d\.\d+)")
success_pattern = re.compile(r"Accepted password.*from (\d+\.\d+\.\d+\.\d+)")

try:
    with open(log_file,"r") as file:
        for line in file:
            failed_match=failed_pattern.search(line)
            success_match=success_pattern.search(line)

            if failed_match:
                ip = failed_match.group(1)
                failed_attempts[ip] += 1

            if success_match:
                ip = success_match.group(1)
                successful_logins[ip] += 1

except FileNotFoundError:
    print(f"Error: File '{log_file}' not found")
    sys.exit(1)


print("\n Failed Login Attempts by IP")
print("--------------------------------")

for ip, count in failed_attempts.items():
    print(f"{ip} : {count}")

print("\n Successful Logins by IP")
print("--------------------------------")

for ip, count in successful_logins.items():
    print(f"{ip} : {count}")

print("\n Suspicious IPs (More than 5 failed attempts)")
print("--------------------------------")

for ip, count in failed_attempts.items():
    if count > 5:
        print(f"ALERT: {ip} has {count} failed login attempts")

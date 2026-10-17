import re
import os

LOG_FILE = "../Defensive-Security-Incident-Response/logs/access_audit.log"
print("--- CYBERSECURITY CAPSTONE: AUTOMATED LOG ANALYZER ---")

if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()
    print(f"[+] Loaded {len(logs)} log entries for forensic analysis.")
    
    print("\n[*] Scanning for Brute-Force Indicators (HTTP 401):")
    for line in logs:
        if "401" in line:
            print(f"  [ALERT] Brute-Force Attempt Detected -> {line.strip()}")
            
    print("\n[*] Scanning for SQL Injection Payloads:")
    for line in logs:
        if "UNION SELECT" in line:
            print(f"  [CRITICAL] SQLi Payload Detected -> {line.strip()}")
else:
    print("[-] Access log not found. Ensure Module 5 logs are present.")

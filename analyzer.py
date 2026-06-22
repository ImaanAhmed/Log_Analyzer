import re
import csv
from collections import Counter

ip_list = []

file = open("server_logs.txt", "r")
for line in file:
    if "Failed password" in line:
        ipgrabber = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if ipgrabber:
            ip_list.append(ipgrabber.group())

tally = Counter(ip_list)
print(tally)

threat_report = open("threat_report.csv", "w", newline="")
writer = csv.writer(threat_report)
writer.writerow(["IP Address", "Failed Attempts"])

for ip, count in tally.items():
    writer.writerow([ip, count])

threat_report.close()

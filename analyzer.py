import re
import csv
import argparse 
from collections import Counter

parser = argparse.ArgumentParser(description="Parse server logs for failed SSH logins.")
parser.add_argument("-i", "--input", default="server_logs.txt", help="Path to the input log file")
parser.add_argument("-o", "--output", default="threat_report.csv", help="Path to the output CSV")
args = parser.parse_args()

ip_list = []

file = open(args.input, "r")
for line in file:
    if "Failed password" in line:
        ipgrabber = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if ipgrabber:
            ip_list.append(ipgrabber.group())
file.close()

tally = Counter(ip_list)
print(tally)

threat_report = open(args.output, "w", newline="")
writer = csv.writer(threat_report)
writer.writerow(["IP Address", "Failed Attempts"])

for ip, count in tally.items():
    writer.writerow([ip, count])

threat_report.close()

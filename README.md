# SSH Log Analyzer

A straightforward Python script that scans server logs for failed SSH login attempts. It extracts the offending IP addresses, counts how many times they tried to connect, and exports a clean CSV report so you can easily spot brute-force attacks.

## Why it's useful
Instead of manually reading through thousands of lines of server logs, this tool automates the process. It finds the "Failed password" lines, pulls out the IPv4 addresses, and ranks them by frequency.

## Usage

Run it with the default files (reads `server_logs.txt` and writes to `threat_report.csv`):

    python analyzer.py

Or specify your own input and output files:

    python analyzer.py -i /var/log/auth.log -o report.csv

## Tech Stack
* Written in standard **Python 3**.
* Uses built-in libraries (`re`, `csv`, `argparse`, `collections`).
* Zero external dependencies (no `pip install` required).

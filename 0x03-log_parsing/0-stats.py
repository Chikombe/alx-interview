#!/usr/bin/env python3
import sys
import signal
import re

# Regular expression to validate and parse log lines
log_pattern = re.compile(
    r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

# Dictionary to store the count of status codes
status_counts = {}
# Variable to store the total file size
total_file_size = 0
# List of valid status codes
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
# Counter to track number of lines processed
line_count = 0

def print_stats():
    """Print the current statistics"""
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_counts):
        if status_code in valid_status_codes:
            print("{}: {}".format(status_code, status_counts[status_code]))

def signal_handler(sig, frame):
    """Handle the SIGINT signal to gracefully terminate the script"""
    print_stats()
    sys.exit(0)

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            # Update the total file size
            total_file_size += file_size

            # Update the count of the status code
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            # Update the line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f'An error occurred: {e}', file=sys.stderr)

# Print final statistics if script ends without interruption
print_stats()


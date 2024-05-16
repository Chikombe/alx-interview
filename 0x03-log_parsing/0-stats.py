#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    file_size, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) >= 2:
                # Extract status code
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
                # Extract file size
                try:
                    file_size += int(data[-1])
                except ValueError:
                    pass
            if count % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)
    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise

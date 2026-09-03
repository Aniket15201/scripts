#!/usr/bin/env python3
"""
Simple test script for Cronicle job testing.
Prints a timestamped message and a counter loop, then exits.
"""

import datetime
import time
import sys

def main():
    start_time = datetime.datetime.now()
    print(f"===== Script started at {start_time} =====")

    for i in range(1, 6):
        print(f"Step {i}/5: doing some work...")
        time.sleep(1)

    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()

    print(f"===== Script finished at {end_time} =====")
    print(f"Total duration: {duration} seconds")
    print("SUCCESS: Script completed without errors.")

    return 0

if __name__ == "__main__":
    sys.exit(main())

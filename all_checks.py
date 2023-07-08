#!/usr/bin/env python

import os
import sys

def check_reboot():
    "Returns true if the computer has a pending reboot."
    return os.path.exists("/run/reboot-required")

def main():
     if check_reboot():
         print("Pending Reboot.")
         sys.exit(1)
     else:
         print("Everything Ok.")
         sys.exit(0)

if __name__ == "__main__":
    main()

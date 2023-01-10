#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
For - Loppong across a file opened with 'with'"""

with open("dnsservers.txt", "r") as dnsfile:
    dnslist = dnsfile.readlines()
    for svr in dnslist:
        print(svr, end="")


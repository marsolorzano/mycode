#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ")
# this line now prompts the usr for input

# a proided string will test true
if ipchk:
    print("Looks like the IP address was set: " + ipchk)
else: #if data is NOT provided
    print("You did not provide input.") 

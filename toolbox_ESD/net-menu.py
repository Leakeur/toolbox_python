import os 
from netconfig_tools import *


net_list = list_net_card()

print("*************************************************")
print("                Make your choice                 ")
print("1) Enable / Disable your network interfaces      ")
print("2) Configure your network interfaces             ")
print("*************************************************")

if raw_input() == 1:
    up_down_card()

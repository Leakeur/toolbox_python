import os 
from netconfig_tools import *


net_list = list_net_card()

print("*******************************************")
print("                Make your choice           ")
print("1) Enable / Disable your network interfaces")
print("2) Configure your network interfaces       ")
print("3) See your ip address                     ")
print("4) Change your Mac address                 ")
print("5) See your public IP                      ")
print("6) Enable Anon Surf                        ")
print("7) Disable Anon Surf                       ")
print("8) Reset   Anon Surf                       ")
print("*******************************************")

def launch_menu():        
    read_cmd = input()
    if read_cmd == 1:
        up_down_card(net_list)
    elif read_cmd == 2:
        set_ip(net_list)
    elif read_cmd == 3:
        show_ifconfig()
    elif read_cmd == 4:
        change_mac(net_list)   
    elif read_cmd == 5:
        get_pub_ip()
    elif read_cmd == 6:
        enable_anon()    
    elif read_cmd == 7:
        disable_anon()
    elif read_cmd == 7:
        reset_anon()            
    else:
        print("Bad number")
        launch_menu()
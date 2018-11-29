# /usr/bin/python 

import os,random, time
from urllib.request import urlopen


global net_list

#Function to switch up / down for network cards 
def up_down_card(net_list):
    print("You have actually these network interfaces : " + str(net_list) ) 
    for net_card in net_list:
        print ("Please enter a value for interface "+ net_card +  "\n")    
        value = int(input('1 for enable, 0 for disable : '))
        if value == 1:
            try:    
                os.system("ifup " + net_card)
            except ValueError:
                print ("Oops ! There is a problem, please check your network configuration")
        elif value == 0:
            try:    
                os.system("ifdown " + net_card)
            except ValueError:
                print ("Oops ! There is a problem, please check your network configuration")
        else:
            print ("Not 0 or 1" + "\n") 
            up_down_card(net_list)
    
    
#Function to list all network adaptater on your device 
def list_net_card():
    net_list = os.listdir("/sys/class/net")
    return net_list

#Function to set configuration on all network adaptater    
def set_ip(net_list):
    #delete currently /etc/network/interfaces file 
    os.system("rm /etc/network/interfaces")
    #create a new one 
    net_file = open('/etc/network/interfaces','w+')
    net_file.write("#For more information, see interfaces(5) \n#source /etc/network/interfaces.d/* \n \n")
    net_file.write("#The loopack network interface \nauto lo\niface lo inet loopback \n \n")
    for net_card in net_list:
        if net_card != "lo":
            print("Welcome to the network configuration for your interface " + net_card + '\n')    
            value = str(input('Do you want to configure your interface in dhcp or static ? : '))
            #Configuration if the choice was DHCP 
            if value == "dhcp":
                net_card_dhcp = ("auto "+ net_card + "\n" + "iface "+ net_card + " inet dhcp")
                net_file.write(net_card_dhcp + "\n" + "\n")
            #Confifguration if the choice was static 
            elif value == "static":
                ip_addr = input('Please enter the IP address (Format xxx.xxx.xxx.xxx) : ')
                netmask = input('Please enter the Netmask of your network (Format xxx.xxx.xxx.xxx) : ')
                gateway = input('Please enter the IP address of your Gateway (Format xxx.xxx.xxx.xxx : ')
                net_card_static = ("auto "+ net_card + "\n" + "iface " + net_card + " inet static" + "\n" + "address " + ip_addr + "\n" + "netmask " + netmask + "\n" + "gateway " + gateway + "\n")
                net_file.write(net_card_static + "\n" + "\n")
            else:
                print ("Not dhcp or static")
                set_ip(net_card) 
    net_file.close()       
    os.system("cat /etc/network/interfaces")
    os.system("/etc/init.d/networking restart")

#function to show ip config 
def show_ifconfig():
    os.system("ifconfig -a")

#funciton to change mac address of one network adaptater 
def change_mac(net_list):
    print (net_list)
    choice = input ("Choose the interface you want to change mac address : ")
    if choice == "lo":
        print("nothing to do for lo")
    else:
        mac_unformat = randomMAC()
        mac_format = MACprettyprint(mac_unformat)
        os.system("ifconfig " + choice + " hw ether " + mac_format)
        print("Your address mac for " + choice + " has been replaced by " + mac_format)

#Function to generate a random mac address 
def randomMAC():
    return [ 0x00, 0x50, 0x56,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]

#Function to format mac address to debian format 
def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))
    #joint everything with :

#Function to get public ip 
def get_pub_ip():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    print ("This is your public ip : " + str(my_ip,'UTF-8'))

#Function to enable anon surf for connecting to tor network 
def enable_anon():
    #If anonsurf is not already install, we will install it 
    if os.system("anonsurf start") != 0:
        print("AnonSurf does not exist on your system, we will install it")
        time.sleep(10)
        os.system("mkdir /root/anonsurf")
        os.system("cd /root/anonsurf && wget https://github.com/Und3rf10w/kali-anonsurf/archive/master.zip")
        os.system("cd /root/anonsurf && unzip master.zip")
        os.system("cd /root/anonsurf/kali-anonsurf-master/ && ./installer.sh")
        time.sleep(2)
        os.system("rm -r /root/anonsurf")
        os.system("rm libjetty8-java_8.1.16-4_all.deb")
        time.sleep(2)
        os.system("anonsurf start")
    else:
        os.system("anonsurf start")

#Function to disable anon surf 
def disable_anon():
    os.system("anonsurf stop")

#Function to reset anon surf (change public ip)
def reset_anon():
    os.system("anonsurf change")        

def launch_menu(): 
    net_list = list_net_card()       
    read_cmd = int(input())
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
    elif read_cmd == 8l:
        reset_anon()            
    else:
        print("Bad number")
        launch_menu()    


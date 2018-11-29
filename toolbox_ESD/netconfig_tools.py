# /usr/bin/python 

import os,random, time
from urllib2 import urlopen


global net_list

def up_down_card(net_list):
    print("You have actually these network interfaces : " + str(net_list) ) 
    for net_card in net_list:
        print ("Please enter a value for interface "+ net_card +  "\n")    
        value = int(raw_input('1 for enable, 0 for disable : '))
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
    
    

def list_net_card():
    net_list = os.listdir("/sys/class/net")
    return net_list
    
def set_ip(net_list):
    os.system("rm /etc/network/interfaces")
    net_file = open('/etc/network/interfaces','w+')
    net_file.write("#For more information, see interfaces(5) \n#source /etc/network/interfaces.d/* \n \n")
    net_file.write("#The loopack network interface \nauto lo\niface lo inet loopback \n \n")
    for net_card in net_list:
        if net_card != "lo":
            print("Welcome to the network configuration for your interface " + net_card + '\n')    
            value = str(raw_input('Do you want to configure your interface in dhcp or static ? : '))
            if value == "dhcp":
                net_card_dhcp = ("auto "+ net_card + "\n" + "iface "+ net_card + " inet dhcp")
                net_file.write(net_card_dhcp + "\n" + "\n")
            elif value == "static":
                ip_addr = raw_input('Please enter the IP address (Format xxx.xxx.xxx.xxx) : ')
                netmask = raw_input('Please enter the Netmask of your network (Format xxx.xxx.xxx.xxx) : ')
                gateway = raw_input('Please enter the IP address of your Gateway (Format xxx.xxx.xxx.xxx : ')
                net_card_static = ("auto "+ net_card + "\n" + "iface " + net_card + " inet static" + "\n" + "address " + ip_addr + "\n" + "netmask " + netmask + "\n" + "gateway " + gateway + "\n")
                net_file.write(net_card_static + "\n" + "\n")
            else:
                print ("Not dhcp or static")
                set_ip(net_card) 
    net_file.close()       
    os.system("cat /etc/network/interfaces")
    os.system("/etc/init.d/networking restart")


def show_ifconfig():
    os.system("ifconfig -a")

def change_mac(net_list):
    print (net_list)
    choice = raw_input ("Choose the interface you want to change mac address : ")
    if choice == "lo":
        print("nothing to do for lo")
    else:
        mac_unformat = randomMAC()
        mac_format = MACprettyprint(mac_unformat)
        os.system("ifconfig " + choice + " hw ether " + mac_format)
        print("Your address mac for " + choice + " has been change")

def randomMAC():
    return [ 0x00, 0x50, 0x56,
            random.randint(0x00, 0x7f),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]

#generates 3 random numbers with 3 default numbers
def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))
    #joint everything with :

def get_pub_ip():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    print ("This is your public ip : " + my_ip)

def enable_anon():
    if os.system("anonsurf start") != 0:
        print("AnonSurf does not exist on your system, we will install it")
        time.sleep(10)
        os.system("mkdir /root/anonsurf")
        os.system("cd /root/anonsurf && wget https://github.com/Und3rf10w/kali-anonsurf/archive/master.zip")
        os.system("cd /root/anonsurf && unzip master.zip")
        os.system("cd /root/anonsurf/kali-anonsurf-master/ && ./installer.sh")
        time.sleep(2)
        os.system("rm -r /root/anonsurf")
        time.sleep(2)
        os.system("anonsurf start")
    else:
        os.system("anonsurf start")

def disable_anon():
    os.system("anonsurf stop")

def reset_anon():
    os.system("anonsurf change")        

#!/usr/bin/python3
from scapy.all import *
from netifaces import AF_INET
import netifaces as ni
import ipaddress

#Request interface for the scan
try:
	print("\n\nAvailable interfaces :")
	print(ni.interfaces())

	choix = input("Choose your network card :")

	ip = ni.ifaddresses(choix)[AF_INET][0]['addr']
	mask = ni.ifaddresses(choix)[AF_INET][0]['netmask']

	cidr = ipaddress.ip_interface(ip + '/' + mask)

#Network search
	for host in ipaddress.IPv4Network(str(cidr.network)):
		arpRequete = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(host), hwdst="ff:ff:ff:ff:ff:ff")
		arpReponse = srp1(arpRequete, timeout=1, verbose=0)

#Show if a return is found
		if arpReponse :
			print ("IP: " + arpReponse.psrc + "\t MAC: " + arpReponse.hwsrc)

#to avoid troll
except:
	print("You have to select a network card available...")

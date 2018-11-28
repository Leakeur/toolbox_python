#!/usr/bin/python3
from scapy.all import *
from netifaces import AF_INET
import netifaces as ni
import ipaddress

#Demander l'interface pour le scan
try:
	print("\n\nInterface Disponible :")
	print(ni.interfaces())
	choix = input("Choisir la carte :")
	ip = ni.ifaddresses(choix)[AF_INET][0]['addr']
	mask = ni.ifaddresses(choix)[AF_INET][0]['netmask']
	cidr = ipaddress.ip_interface(ip + '/' + mask)

	for host in ipaddress.IPv4Network(str(cidr.network)):
		arpRequete = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(host), hwdst="ff:ff:ff:ff:ff:ff")
		arpReponse = srp1(arpRequete, timeout=1, verbose=0)

#Si réponse, afficher l'@ IP et l'@ MAC des hosts trouvé
	if arpReponse :
		print ("IP: " + arpReponse.psrc + "\t MAC: " + arpReponse.hwsrc)

except:
	print("Il faut selectionner une interface disponible...")

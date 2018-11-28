#!/usr/bin/python3

import socket, struct, binascii

def AnalyseETH(entete):
        ent_eth = struct.unpack("!6s6s2s", entete)
        source = binascii.hexlify(ent_eth[0]).decode()
        dest = binascii.hexlify(ent_eth[1]).decode()
        print ("\nEthernet")
        print ("-Source:\t ", source)
        print ("-Destination:\t\t ", dest)

        if ent_eth[2] == b'\x08\x00':
                return True

def AnalyseIP(entete):
        ip_hdr = struct.unpack("!9s1s2s4s4s", entete)
        source = socket.inet_ntoa(ip_hdr[3])
        dest = socket.inet_ntoa(ip_hdr[4])

        print ("\nIP")
        print ("-Source:\t ", source)
        print ("-Destination:\t\t ", dest)

        if binascii.hexlify(ip_hdr[1]).decode() == '06':
                return True

        elif binascii.hexlify(ip_hdr[1]).decode() == '11':
                return False

def AnalyseTCP(entete):
        tcp_hdr = struct.unpack("!HH16s", entete)
        src_port,dst_port,lereste = tcp_hdr


        print ("\nTCP")
        print ("-Port Source:\t\t", src_port)
        print ("-Port Destination:\t", dst_port)
        if (src_port == 80 ) or (dst_port == 80):
                return True

def AnalyseUDP(entete):
        udp_hdr = struct.unpack("!HH16s", entete)
        src_port,dst_port,lereste = udp_hdr
        print ("\nUDP")
        print ("-Port Source:\t\t", src_port)
        print ("-Port Destination:\t", dst_port)


def AnalyseHTTP(data):
        print (data)


rawSock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
while True:
        pkt = rawSock.recvfrom(2048)
        print ("\n------------------------------------------\n")
        print ("Packet Recu:")
        enteteL2,enteteL3,enteteL4,HTTP=pkt[0][0:14],pkt[0][14:34],pkt[0][34:54],pkt[0][54:]
        if AnalyseETH(enteteL2):

                if AnalyseIP(enteteL3):

                        if AnalyseTCP(enteteL4):
                                AnalyseHTTP(HTTP)
                else :
                        AnalyseUDP(enteteL3)
        print ("\nTerminé!\n\n")
        print ("\n------------------------------------------\n")

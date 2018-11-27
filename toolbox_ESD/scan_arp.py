# -*- coding: utf-8 -*-
import socket, sys

HOST = '192.168.109.128'
PORT = 50000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "La liaison du socket à l'adresse choisie a échoué."
    sys.exit()

while 1:
    print "Serveur prêt, en attente de requêtes ..."
    mySocket.listen(5)
    
    connexion, adresse = mySocket.accept()
    print "Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1])
    
    connexion.send("Vous êtes connecté au serveur Marcel. Envoyez vos messages.")
    msgClient = connexion.recv(1024)
    while 1:
        print "C>", msgClient
        if msgClient.upper() == "FIN" or msgClient =="":
            break
        msgServeur = raw_input("S> ")
        connexion.send(msgServeur)
        msgClient = connexion.recv(1024)

    connexion.send("Au revoir !")
    print "Connexion interrompue."
    connexion.close()

    ch = raw_input("<R>ecommencer <T>erminer ? ")
    if ch.upper() =='T':
        break

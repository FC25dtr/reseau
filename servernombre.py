import random 
import socket 
import sys 

Host = '10.9.186.30'
PORT = 2009
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #AF_INET socket avec protocole IP STREAM = protocole TPC
try:
    mySocket.bind((Host, PORT)) #cree donc si on veut connecte on .connect
except socket.error:
    print(" La liaison du socket à l'adresse choisie a echoué. ")
    sys.exit()

while 1:
    print("le server est actuellement en attente...")
    mySocket.listen(5) # nbr de machine connecté 
    connexion, adresse = mySocket.accept() #accepte renvoi un tuple 
    print("Un client est connecté depuis l'adresse IP {} et le port {}".format(adresse[0], adresse[1])) # adresse est un tuple ip et port
    connexion.send(("Vous êtes connecté au serveur " + Host + ":" + str(PORT) +".\n").encode('UTF-8')) #message à l'utilisateur 
    connexion.send("le nombre maximum ? \n.".encode('UTF-8'))
    nbr_max = connexion.recv(1024) #convertie d'un tableau d'octet en chaine de caractère. recois une entree de l'utilisateur 
    nbr_max = int(nbr_max)
    nbr_test = random.randrange(0,nbr_max)
    while 1:
        connexion.send("essayer un nombre. \n".encode('UTF-8'))
        nbr_user = connexion.recv(1024) #convertie d'un tableau d'octet en chaine de caractère.
        nbr_user = int(nbr_user)
        if nbr_user > nbr_test :
            print("moin, ")
            a = "moin, "
        elif nbr_user < nbr_test :
            print("plus")
            a = "plus"
        else:
            break 
        connexion.send(("ECHO : "+ a).encode('UTF-8'))
    connexion.send("trouvé \n".encode('UTF-8'))
    print("Connexion interrompue.")
    # Le serveur ferme la connexion
    connexion.close()

    ch = input("Attendre un autre client ? R(ecommencer)/T(erminer) ? ")
    if ch.upper() == 'T':
        break

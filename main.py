from objects import *

#id=1
#prev= "0000000000000000000000000000000000000000000000000000000000000000"
content= "la blockchain marche ?"
sign= "guillaume"

def read():
    with open('chain.txt','r') as rf:
        lastBlock=rf.readlines()[-1]
        sep=lastBlock.split(",")
    return sep
    
def addBlock(content,sign):
    Block(read()[0],read()[5],content,sign)

def checkChain():
    with open('chain.txt','r') as rf:
        chain=rf.readlines()
        for i in range(len(chain)-1):
            print(chain[i].split(",")[-2]," == ",chain[i+1].split(",")[1])


def checkBlock():
    with open('chain.txt','r') as rf:
        chain=rf.readlines()
        for i in range(len(chain)):
            data1=""
            for j in range(len(chain[i].split(","))-2):
                data1+=chain[i].split(",")[j]
            hash=hashlib.sha256(data1.encode()).hexdigest()
            if (hash == chain[i].split(",")[-2]):
                verif="VALIDE"
            else:
                verif="ERRONE"
            print("calcul = ",hash," verif = ",chain[i].split(",")[-2]," ",verif)

checkBlock()

addBlock(content,sign)







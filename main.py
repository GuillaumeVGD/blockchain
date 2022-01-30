from objects import *

#id=1
#prev= "0000000000000000000000000000000000000000000000000000000000000000"
content= "la blockchain marche !"
sign= "guillaume"

def read():
    with open('chain.txt','r') as rf:
        lastBlock=rf.readlines()[-1]
        sep=lastBlock.split(",")
    return sep

Block1=Block(read()[0],read()[1],content,sign)







from objects import *

block=1
nonce=0
message="message"
previous="0000000000000000000000000000000000000000000000000000000000000000"

Block1=Block(block,nonce,message,previous)
Block1.signature()
print(Block1.hash)

#def signature(block,nonce,message,previous):
#    data=(message+str(block)+str(nonce))
#    hash= hashlib.sha256(data.encode()).hexdigest()
#    while(str(hash[:4])!="0000"):
#        nonce+=1
#        data=(str(block)+str(nonce)+message+previous)
#        hash=hashlib.sha256(data.encode()).hexdigest()
#        #print(nonce,"   ",hash)
#    return block,nonce,hash,previous
#
#print("final nonce = ",signature(block,nonce,message,previous)[1])
#print("final hash = ",signature(block,nonce,message,previous)[2])


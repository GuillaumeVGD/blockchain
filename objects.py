import hashlib

class Block:
    def __init__(self,block,nonce,message,previous):
        self.block=block
        self.nonce=nonce
        self.message=message
        self.previous=previous
        self.data=(self.message+str(self.block)+str(self.nonce))
        self.hash= hashlib.sha256(self.data.encode()).hexdigest()
        while(str(self.hash[:4])!="0000"):
            self.nonce+=1
            self.data=(str(self.block)+str(self.nonce)+self.message+self.previous)
            self.hash=hashlib.sha256(self.data.encode()).hexdigest()
    
    def show(self):
        print("BLOCK = ",self.block," ; Hash= ",self.hash," ; POF = ", self.nonce," ;")

#class NewBlock:
#    def __init__(self,PrevBlock,message):
#        self.PrevBlock=PrevBlock
#        self.message=message

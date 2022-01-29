import hashlib

class Block:
    def __init__(self,block,nonce,message,previous):
        self.block=block
        self.nonce=nonce
        self.message=message
        self.previous=previous

    def signature(self):
        self.data=(self.message+str(self.block)+str(self.nonce))
        self.hash= hashlib.sha256(self.data.encode()).hexdigest()
        while(str(self.hash[:4])!="0000"):
            self.nonce+=1
            self.data=(str(self.block)+str(self.nonce)+self.message+self.previous)
            self.hash=hashlib.sha256(self.data.encode()).hexdigest()
            #print(nonce,"   ",hash)
        return self.block,self.nonce,self.hash,self.previous

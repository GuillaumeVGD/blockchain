import hashlib

class Block:
    def __init__(self,id,prev,content,sign):
        self.id=id
        self.prev=prev
        self.content=content
        self.sign=sign

        self.pof=0
        self.data=(str(self.id)+str(self.prev)+str(self.content)+str(self.sign)+str(self.pof))
        self.hash= hashlib.sha256(self.data.encode()).hexdigest()
        
        while(str(self.hash[:4])!="0000"):
            self.pof+=1
            self.data=(str(self.id)+str(self.prev)+str(self.content)+str(self.sign)+str(self.pof))
            self.hash=hashlib.sha256(self.data.encode()).hexdigest()
    
    def show(self):
        print("ID = ",self.id," ; PREV = ",self.prev," ; CONTENT = ", self.content," ; SIGN = ",self.sign," ; POF = ",self.pof," ; HASH = ",self.hash," ;")



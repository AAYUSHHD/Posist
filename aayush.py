import datetime #for timestamp functionality

class node(object);
def _init_selfpractice_(self, data, nodeNumber, nodeid, genesisReferenceNodeiId);
    self.timestamp=datetime.datetime.now()
    sel.data=data
    self.nodenumver=nodenumber
    self.nodeid=nodeid
    self.referenceNodeid=None
    self.childReferenceNode=[]
    self.genesisReferenceNodeiId=genesisReferenceNodeiId
    self.hashvalue=None
    
    
    
    
    class guts(object):
        def _init_(self, owner):
            self.nodeid=# -*- coding: latin-1 -*-self.owner=owner
            
            
        def creatgenesis(self):          #answer1
            self.genesisnode=node(None,nodeid,"genesis",None)
            self.genesisnode, referenceNodeid=None
            
            
            
        def createsetofchildnodes(self,datalist,nodecounter,ofparent,namelist):
            for i in range(len(namelist)):
                child+node(datalist[i],nodecounter,namelist[i],self.genesisRferenceNodeid)            #answer 2
                ofparent.childReferenceNodeid.append(childReferenceNodeid)
                self.nodecounter += 1 
                
                
                
                
        def createchild(self,data,nodecounter,ofparent,namew):
            child=node(data,nodecounter,name,sekf.genesisRferenceNodeid)                     #answer 3
            ofparent.childReferenceNodeid.append(child)
            self.nodecounter += 1 
            
            
            
            
            
        def heapify(n, i):
    global list
    largest = i
    L = 2 * i + 1                                                                   #answer 8
    r = 2 * i + 2
    if L < n and list[i] < list[L]:
        largest = L
    if r < n and list[largest] < list[r]:
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]    
                
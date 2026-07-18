class Node:
    def __init__(self,key,val):
        self.key, self.val, = key,val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to the node

        #left = LRU, Right = MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right,self.left
        
    #remove node from list
    def remove(self,node):
        prv,nxt = node.prev, node.next
        prv.next, nxt.prev = nxt,prv

    #insert at right (MRU)
    def insert(self,node):
        prv,nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.next = nxt
        node.prev = prv
       


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove from linkedlist and delete lru from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        

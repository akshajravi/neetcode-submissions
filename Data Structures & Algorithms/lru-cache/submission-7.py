class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    
    def _insert(self,node):
        temp = self.right.prev
        self.right.prev = node
        node.next = self.right 
        node.prev = temp
        temp.next = node
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

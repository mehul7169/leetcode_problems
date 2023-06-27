from collections import deque

class LinkNode:
    def __init__(self, index = -1, num = -1):
        self.val = num
        self.key = index
        self.next = None
        self.prev = None

class LRUCache:       
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cur = 0
        self.keys = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key in self.keys:
            self.move(self.keys[key])
            return self.keys[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.keys:
            self.keys[key].val = value
            self.move(self.keys[key])
        else:
            node = ListNode(key, value)
            self.add(node)
            self.keys[key] = node
            self.cur += 1
        if self.cur > self.cap:
            self.popLast()
            self.cur -= 1
        
    def add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
        

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
         
    def move(self, node):
        self.delete(node)
        self.add(node)
    
    def popLast(self):
        self.keys.pop(self.tail.prev.key)
        self.delete(self.tail.prev)
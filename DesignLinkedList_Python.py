class LinkNode():
    def __init__(self, val = -1):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index + 1):
            if curr == self.tail:
                return -1
            curr = curr.next
        return curr.val


    def addAtHead(self, val: int) -> None:
        node = LinkNode(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        node = LinkNode(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = LinkNode(val)
        curr = self.head
        for i in range(index):
            if curr == self.tail:
                return
            curr = curr.next
        if curr == self.tail:
                return
        node.next = curr.next
        node.prev = curr
        curr.next.prev = node
        curr.next = node
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        for i in range(index):
            if curr == self.tail:
                return
            curr = curr.next
        if curr == self.tail:
                return
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        
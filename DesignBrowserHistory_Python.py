class LinkNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = LinkNode(homepage)
        self.head.next = self.curr
        self.curr.prev = self.head
        self.curr.next = self.tail
        self.tail.prev = self.curr

    def visit(self, url: str) -> None:
        node = LinkNode(url)
        self.curr.next = node
        node.next = self.tail
        node.prev = self.curr
        self.tail.prev = node
        self.curr = node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr == self.head:
                self.curr = self.head.next
                return self.curr.val
            self.curr = self.curr.prev
        if self.curr == self.head:
            self.curr = self.head.next
            return self.curr.val
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr == self.tail:
                self.curr = self.tail.prev
                return self.curr.val
            self.curr = self.curr.next
        if self.curr == self.tail:
            self.curr = self.tail.prev
            return self.curr.val
        
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = r = head
        if not head:
            return head
        size = 0
        for i in range(k):
            if r.next != None:
                r = r.next
                size += 1
            else:
                r = head
                size += 1
                break
        
        if k > size:
            k = k % size

            r = head
            for i in range(k):
                r = r.next

        if l == r:
            return head
        while r.next:
            l, r = l.next, r.next
        
        for i in range(k):
            r.next = head
            head = r
            r = l
            while r.next != head:
                r = r.next
        l.next = None
        
        return head
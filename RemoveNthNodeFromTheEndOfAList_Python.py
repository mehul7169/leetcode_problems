class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head

        for i in range(n):
            r = r.next

        if not r:
            head = head.next
        else:
            while r.next:
                l = l.next
                r = r.next
            l.next = l.next.next
        return head
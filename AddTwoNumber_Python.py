# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        cur = head
        carry = 0
        while l1 or l2 or carry:
            l1Num = l1.val if l1 else 0
            secondNum = l2.val if l2 else 0

            total = l1Num + secondNum + carry
            carry = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur.next = ListNode(total % 10)
            cur = cur.next

            
        return head.next
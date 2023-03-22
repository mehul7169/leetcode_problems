class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return ListNode().next
        head = ListNode()
        head.val = None
        cur = head
        while list1 != None or list2 != None:
            nextNode = ListNode()
            if list1 == None:
                cur.val = list2.val
                if list2.next == None:
                    break
                list2 = list2.next
            elif list2 == None:
                cur.val = list1.val
                if list1.next == None:
                    break
                list1 = list1.next
            elif list1.val < list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
            cur.next = nextNode
            cur = nextNode
        return head
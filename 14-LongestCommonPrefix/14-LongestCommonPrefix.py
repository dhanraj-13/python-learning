# Last updated: 8/24/2026, 3:48:42 PM
1class Solution:
2    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
3        dummy = temp = ListNode(0)
4        while l1 != None and l2 != None: #1
5
6            if l1.val < l2.val: #2
7                temp.next = l1 #3
8                l1 = l1.next #4
9            else: 
10                temp.next = l2
11                l2 = l2.next
12            temp = temp.next
13        temp.next = l1 or l2  #5
14        return dummy.next #6
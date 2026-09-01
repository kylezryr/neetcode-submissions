# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        resultPointer = result

        while list1 != None and list2 != None:
            list1Val = 101 if list1 is None else list1.val
            list2Val = 101 if list2 is None else list2.val

            if list1Val < list2Val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next

            result = result.next

        result.next = list1 or list2

        return resultPointer.next
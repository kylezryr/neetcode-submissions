# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def mergeLists(l1, l2):
            sentinel = ListNode()
            headPtr = sentinel

            while l1 != None or l2 != None:
                l1Val = l1.val if l1 != None else float("inf")
                l2Val = l2.val if l2 != None else float("inf")

                if l1Val < l2Val:
                    sentinel.next = l1
                    l1 = l1.next
                else:
                    sentinel.next = l2
                    l2 = l2.next
                sentinel = sentinel.next
            
            return headPtr.next

        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_l1_l2 = mergeLists(l1, l2)
                mergedLists.append(merged_l1_l2)
            lists = mergedLists
        
        return lists[0]



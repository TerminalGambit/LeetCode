"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            
            # Create a dummy node and a pointer to it
            dummy = ListNode()
            pointer = dummy
            
            # Loop through both lists
            while list1 and list2:
                
                # If the value of list1 is less than list2
                if list1.val < list2.val:
                    
                    # Set the pointer's next node to list1
                    pointer.next = list1
                    
                    # Move list1 forward
                    list1 = list1.next
                    
                # If the value of list2 is less than list1
                else:
                    
                    # Set the pointer's next node to list2
                    pointer.next = list2
                    
                    # Move list2 forward
                    list2 = list2.next
                    
                # Move the pointer forward
                pointer = pointer.next
                
            # If list1 is not empty, set the pointer's next node to list1
            if list1:
                pointer.next = list1
                
            # If list2 is not empty, set the pointer's next node to list2
            if list2:
                pointer.next = list2
                
            # Return the dummy node's next node
            return dummy.next
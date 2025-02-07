# Question:
# Ek linked list di gayi hai, usse reverse karna hai.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    return prev

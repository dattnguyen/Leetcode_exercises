# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    cur = head #start the pointer
    while cur: #traverse the linked list
        while cur.next and cur.next.val == cur.val: #if the two values of the two consecutive nodes are equal
            cur.next = cur.next.next # point to node that is next to the next node
        cur = cur.next #move the pointer along
    return head



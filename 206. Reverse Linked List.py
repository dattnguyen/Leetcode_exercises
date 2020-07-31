# Reverse a singly linked list.

def reverseList(self, head: ListNode) -> ListNode:
    cur = head #create a pointer
    while cur.next != None: #traverse through the linked list
        temp = cur.next.next #remember the cur.next.next to relink after pushing cur.next to the top
        cur.next.next = head #pushing the cur.next to the top
        head = cur.next #update the new head for future push
        cur.next = temp #relink after pushing

    return head
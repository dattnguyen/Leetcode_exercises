l1 = [2, 4, 6, 7]
l2 = [1, 2, 3]

lall = l1 + l2
print (sorted(lall))
#%%
def mergeTwoLists(l1, l2):
    lall = l1 + l2
    return print(sorted(lall))
l1 = [2, 4, 6, 7]
l2 = [1, 2, 3]
mergeTwoLists (l1,l2)

#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists1(l1: ListNode, l2:ListNode):
    cur = ListNode(0)
    dummy = cur #create a dummy list that contains the new merged sorted data as we go along the list

    while l1 and l2: #when both of the linked lists are not Null
        if l1.val < l2.val: #if l1 less than l2, point at the lesser value
            cur.next = l1
            l1 = l1.next #move the pointer at l1 to the next
        else:
            cur.next = l2 #see above
            l2 = l2.next
        cur = cur.next #also need to move the dummy pointer

    cur.next = l1 or l2 #in case we finish 1 linked list and there are still elements in the other
                        #we just need to grab those elements and link it to the result linked list

    return dummy.next
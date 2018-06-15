# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    res = reverseList(head.next)
    head.next.next = head
    print(head.val, head.next.val)
    return res

#x = reverseList(a)

# 变种reverse print list
def reversePrint(node):
    if not node:
        return
    reversePrint(node.next)
    print(node.val)
reversePrint(a)

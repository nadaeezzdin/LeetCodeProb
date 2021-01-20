"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1, l2) :
    outList = currentNode = ListNode(0)
    carry = sum = 0 
    while l1 or l2 or carry:
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2= l2.next
         
        carry = sum // 10
        sum = sum % 10
        
        
        currentNode.next = ListNode(sum)
        currentNode = currentNode.next
        sum = carry
        carry = 0
    return outList.next


print(addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))

         




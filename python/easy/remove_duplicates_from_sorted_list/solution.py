# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


solution = Solution()

# Testcase 1
head = ListNode(1, ListNode(1, ListNode(2)))
res = solution.deleteDuplicates(head)
print_list(res)
print(res == ListNode(1, ListNode(2)))

# Testcase 2
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
res = solution.deleteDuplicates(head)
print_list(res)
print(res == ListNode(1, ListNode(2, ListNode(3))))

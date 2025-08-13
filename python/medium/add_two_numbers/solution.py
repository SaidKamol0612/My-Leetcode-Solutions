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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dump_head = ListNode(0)
        current = dump_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            current.next = ListNode(new_val)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dump_head.next


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


solution = Solution()

# Testcase 1
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
res = solution.addTwoNumbers(l1, l2)
print_list(res)
print(res == ListNode(7, ListNode(0, ListNode(8))))  # Explanation: 342 + 465 = 807.

# Testcase 2
l1 = ListNode(0)
l2 = ListNode(0)
res = solution.addTwoNumbers(l1, l2)
print_list(res)
print(res == ListNode(0))

# Testcase 3
l1 = ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
)
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
res = solution.addTwoNumbers(l1, l2)
print_list(res)
print(
    res
    == ListNode(
        8,
        ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
            ),
        ),
    )
)

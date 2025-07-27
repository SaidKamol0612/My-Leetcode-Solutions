class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        res = []
        for i in range(len(nums)):
            if nums[i] != val:
                res.append(nums[i])
        nums[:] = res
        return len(nums)


solution = Solution()


# Custom judge
def test_removeElement(n, v, e):
    nums = n  # Input array
    val = v  # Value to remove
    expected_nums = e  # The expected answer with correct length

    k = solution.removeElement(nums, val)  # Calls the your implementation

    assert k == len(expected_nums)
    sorted(nums)  # Sort the first k elements of nums
    for i in range(k):
        assert nums[i] == expected_nums[i]
    return True


# Testcase 1
nums = [3, 2, 2, 3]
val = 3
expected_nums = [2, 2]
res = test_removeElement(nums, val, expected_nums)
print(res)

# Testcase 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
expected_nums = [0, 1, 3, 0, 4]
res = test_removeElement(nums, val, expected_nums)
print(res)

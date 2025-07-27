class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not target in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else:
            return nums.index(target)


solution = Solution()

# Testcase 1
res = solution.searchInsert([1, 3, 5, 6], 5)
print(res, end=" ")
print(res == 2)

# Testcase 2
res = solution.searchInsert([1, 3, 5, 6], 2)
print(res, end=" ")
print(res == 1)

# Testcase 3
res = solution.searchInsert([1, 3, 5, 6], 7)
print(res, end=" ")
print(res == 4)

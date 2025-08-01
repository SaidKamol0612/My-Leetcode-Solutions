class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            x = target - n
            if x == nums[i + 1]:
                return [i, i + 1]
            if x in nums[i + 1:]:
                return [i, nums[i + 1:].index(x) + i + 1]
        return [0]

solution = Solution()
        
# Testcase 1
res = solution.twoSum([2, 7, 11, 15], 9)
print(res, end=' ')
print(res == [0, 1]) # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Testcase 2
res = solution.twoSum([3, 2, 4], 6)
print(res, end=' ')
print(res == [1, 2])

# Testcase 3
res = solution.twoSum([3, 3], 6)
print(res, end=' ')
print(res == [0, 1])
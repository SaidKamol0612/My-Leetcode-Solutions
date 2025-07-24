class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        return int((str(x))[::-1]) == x


solution = Solution()

# Testcase 1
res = solution.isPalindrome(121)
print(res, end=" ")
print(res == True)

# Testcase 2
res = solution.isPalindrome(-121)
print(res, end=" ")
print(res == False)

# Testcase 3
res = solution.isPalindrome(10)
print(res, end=" ")
print(res == False)

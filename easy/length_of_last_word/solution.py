class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.rstrip()
        return len(s.split()[-1])


solution = Solution()

# Testcase 1
res = solution.lengthOfLastWord("Hello World")
print(res, end=" ")
print(res == 5)

# Testcase 2
res = solution.lengthOfLastWord("   fly me   to   the moon  ")
print(res, end=" ")
print(res == 4)

# Testcase 3
res = solution.lengthOfLastWord("luffy is still joyboy")
print(res, end=" ")
print(res == 6)

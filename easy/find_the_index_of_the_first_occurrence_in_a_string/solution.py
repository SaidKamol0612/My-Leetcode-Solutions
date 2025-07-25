class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1

        for i, c in enumerate(haystack):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


solution = Solution()

# Testcase 1
res = solution.strStr("sadbutsad", "sad")
print(res, end=" ")
print(res == 0)

# Testcase 2
res = solution.strStr("leetcode", "leeto")
print(res, end=" ")
print(res == -1)

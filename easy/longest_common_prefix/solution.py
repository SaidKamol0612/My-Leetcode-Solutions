class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = list(set(strs))

        prefix = ""
        i = 0
        while i < len(strs[0]):
            prefix += strs[0][i]
            for s in strs:
                if not s.startswith(prefix):
                    return prefix[: len(prefix) - 1 :] if len(prefix) > 0 else ""
            i += 1
        return prefix


solution = Solution()

# Testcase 1
res = solution.longestCommonPrefix(["flower", "flow", "flight"])
print(res, end=" ")
print(res == "fl")

# Testcase 2
res = solution.longestCommonPrefix(["dog", "racecar", "car"])
print(res, end=" ")
print(res == "")
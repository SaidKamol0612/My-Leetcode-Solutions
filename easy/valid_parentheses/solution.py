class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) < 2 or len(s) % 2 != 0:
            return False

        t = []
        for c in s:
            if c in "([{":
                t.append(c)
            else:
                if not t:
                    return False

                top = t.pop()
                if c == ")" and top != "(":
                    return False
                elif c == "]" and top != "[":
                    return False
                elif c == "}" and top != "{":
                    return False
        return not t


solution = Solution()

# Testcase 1
res = solution.isValid("()")
print(res, end=" ")
print(res == True)

# Testcase 2
res = solution.isValid("()[]{}")
print(res, end=" ")
print(res == True)

# Testcase 3
res = solution.isValid("(]")
print(res, end=" ")
print(res == False)

# Testcase 4
res = solution.isValid("([])")
print(res, end=" ")
print(res == True)

# Testcase 5
res = solution.isValid("([)]")
print(res, end=" ")
print(res == False)

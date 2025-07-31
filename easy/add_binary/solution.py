class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b or len(a) < 1 or len(b) < 1:
            return a or b or "0"

        res = int(a, 2) + int(b, 2)

        return str(bin(res)[2:])

solution = Solution()

# Testcase 1
res = solution.addBinary("11", "1")
print(res, end=" ")
print(res == "100")

# Testcase 2
res = solution.addBinary("1010", "1011")
print(res, end=" ")
print(res == "10101")
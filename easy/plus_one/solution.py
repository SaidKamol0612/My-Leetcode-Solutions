class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for n in digits:
            s += str(n)
        s = str(int(s) + 1)
        res = []
        for c in s:
            res.append(int(c))

        return res

solution = Solution()

# Testcase 1
res = solution.plusOne([1, 2, 3])
print(res, end=" ")
print(res == [1, 2, 4])

# Testcase 2
res = solution.plusOne([4, 3, 2, 1])
print(res, end=" ")
print(res == [4, 3, 2, 2])

# Testcase 1
res = solution.plusOne([9])
print(res, end=" ")
print(res == [1, 0])
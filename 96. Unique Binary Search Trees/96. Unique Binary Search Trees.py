from functools import cache

class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def recur(n):
            if n == 0:
                return 1

            res = 0

            for root in range(1, n + 1):
                res += recur(root - 1) * recur(n - root)

            return res

        return recur(n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, target):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i])
                path.pop()

        backtrack(0, target)
        return res



        
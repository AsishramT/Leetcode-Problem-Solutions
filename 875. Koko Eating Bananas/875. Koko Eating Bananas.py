class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        res = high

        while low <= high:
            hours = 0
            mid = (high + low) // 2

            for p in piles:
                hours += ceil(p/mid)

            if hours <= h:
                res = mid
                high = mid - 1
            elif hours > h:
                low = mid + 1

        return res
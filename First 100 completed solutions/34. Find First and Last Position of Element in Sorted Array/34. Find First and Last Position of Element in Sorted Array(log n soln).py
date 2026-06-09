class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            lo, hi=0, len(nums)
            while lo<hi:
                mid=( lo+ hi )//2
                if nums[mid] < x:
                    lo=mid+1
                else:
                    hi = mid
            return lo
        first = search(target)
        last = search(target+1)-1


        if first<=last:
            return [first,last]

        return[-1,-1]
        
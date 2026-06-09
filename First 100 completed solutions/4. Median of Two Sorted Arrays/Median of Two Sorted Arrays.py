class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_lst=sorted(nums1+nums2)
        length=len(new_lst)
        median=0
        if length%2==0:
            median=(new_lst[length//2]+new_lst[(length//2)-1])/2
        else:
            median=new_lst[length//2]
        return median


        
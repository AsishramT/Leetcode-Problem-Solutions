class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums1[0:m]
        nums2[:]=nums2[0:n]
        if m==0:
            nums1[:]=nums2
        elif n==0:
            nums1.sort()
        else:
            for val in nums2:
                nums1.append(val)
            nums1.sort()


        
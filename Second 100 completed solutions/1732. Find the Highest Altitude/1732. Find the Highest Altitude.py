class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height=0
        start_alt=0

        for altG in gain:
            start_alt+=altG
            max_height=max(start_alt,max_height)
        return max_height
        
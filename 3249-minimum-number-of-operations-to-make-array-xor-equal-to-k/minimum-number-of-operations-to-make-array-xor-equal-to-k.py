class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        dum=0
        for i in nums:
            dum^=i
        dum^=k
        return bin(dum).count("1")
        
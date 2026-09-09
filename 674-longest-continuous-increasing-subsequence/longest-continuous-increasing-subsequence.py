class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        m=1
        l=0
        r=1
        c=1
        while r<len(nums):
            if nums[l]<nums[r]:
                c+=1
                m=max(c,m)
                r+=1
                l+=1
            else:
                l+=1
                r+=1
                c=1
        return m
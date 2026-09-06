class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''ml=0
        for i in range(len(nums)):
            z=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    z+=1
                if z<=k:
                    ml=max(ml,j-i+1)
                else:
                    break
        return ml'''
        ml=0
        l=0
        r=0
        zeros=0
        while r<len(nums):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                ml=max(ml,r-l+1)
            r+=1
        return ml
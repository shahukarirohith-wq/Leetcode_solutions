class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        m=0
        se=set(nums)
        count={x:0 for x in se}
        while r<len(nums):
            if nums[r] in se:
                count[nums[r]]+=1
                while count[nums[r]]>1:
                    count[nums[l]]-=1
                    s-=nums[l]
                    l+=1
            s+=nums[r]
            m=max(m,s)
            r+=1
        return m
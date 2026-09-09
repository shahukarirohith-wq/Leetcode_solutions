class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=0
        ans=0
        frequency={0:1}
        for i in range(len(nums)):
            ps+=nums[i]
            need = ps-k
            if need in frequency :
                ans += frequency[need]
            if ps in frequency:
                frequency[ps] += 1
            else :
                frequency [ps] = 1
        return ans

            
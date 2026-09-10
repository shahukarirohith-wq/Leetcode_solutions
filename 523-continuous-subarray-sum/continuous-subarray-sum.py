class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        freq = {0:-1}
        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k
            if remainder in freq :
                index = i - freq[remainder]
                if index >= 2:
                    return True
            else :
                freq[remainder] = i
        return False
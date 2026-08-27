class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        h=n
        while l<=h:
            mid=(l+h)//2
            ans=guess(mid)
            if ans==0:
                return mid
            elif ans==-1:
                h=mid-1
            else:
                l=mid+1
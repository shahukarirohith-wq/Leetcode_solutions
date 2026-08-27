class Solution1:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        r=0
        ml=0
        f1={}
        while r<len(s):
            if s[r] in f1:
                f1[s[r]]+=1
            else:
                f1[s[r]]=1
            while f1[s[r]]>2:
                f1[s[l]]-=1
                l+=1
            ml=max(ml,r-l+1)
            r+=1
        return ml
            

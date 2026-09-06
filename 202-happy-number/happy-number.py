class Solution:
    def isHappy(self, n: int) -> bool:
        c=0
        def gn(n):
            s=0
            while n>0:
                r=n%10
                s+=r**2
                n//=10
            return s
        a=gn(n)
        while a>=0:
            c+=1
            if a==1:
                return True
            elif c==10:
                return False
            else:
                a=gn(a)
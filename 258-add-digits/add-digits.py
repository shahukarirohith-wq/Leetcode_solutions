class Solution:
    def addDigits(self, num: int) -> int:
        '''s=num
        while s>9:
            num=s
            s=0
            while num>0:
                r=num%10
                s+=r
                num//=10
        return s'''
        def demo(num):
            f=num%10
            r=num//10
            return f+r
        while(num>9):
            num=demo(num)    
        return num

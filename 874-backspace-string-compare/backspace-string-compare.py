class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for ch in s :
            if stack and ch == "#" :
                stack.pop()
            elif not stack and ch == "#" :
                continue
            else :
                stack.append(ch)
        a = "".join(stack)
        stack1 = []
        for ch in t :
            if stack1 and ch == "#" :
                stack1.pop()
            elif not stack1 and ch == "#" :
                continue
            else :
                stack1.append(ch)
        b = "".join(stack1)
        return a == b
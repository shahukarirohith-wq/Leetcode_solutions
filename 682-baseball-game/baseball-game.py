class Solution:
    def calPoints(self, op: list[str]) -> int:
        stack = []
        for ch in op :
            if stack and ch == "+" :
                if len(stack) == 1 :
                    stack.append(stack[-1])
                else :
                    stack.append(stack[-1] + stack[-2])
            elif stack and ch == "D" :
                stack.append(2 * stack[-1])
            elif stack and ch == "C" :
                stack.pop()
            else :
                stack.append(int(ch))
        return sum(stack)
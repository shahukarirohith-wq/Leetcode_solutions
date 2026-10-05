class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimum possible open parentheses count
        cmax = 0  # Maximum possible open parentheses count
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin = max(0, cmin - 1)
                cmax -= 1
            else:  # char == '*'
                cmin = max(0, cmin - 1)  # Treat '*' as ')'
                cmax += 1                # Treat '*' as '('
            if cmax < 0:
                return False 
        return cmin == 0
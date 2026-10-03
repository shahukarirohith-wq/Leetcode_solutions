class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.mini or value <= self.mini[-1] :
            self.mini.append(value)
        else :
            self.mini.append(self.mini[-1])

    def pop(self) -> None:
        if self.stack :
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        if self.stack :
            return self.stack[-1]

    def getMin(self) -> int:
        if self.mini :
            return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
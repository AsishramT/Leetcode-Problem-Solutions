class MyQueue:

    def __init__(self):
        self.stackIN = []
        self.stackOUT = []

    def push(self, x: int) -> None:
        self.stackIN.append(x)

    def pop(self) -> int:
        if not self.stackOUT:
            while self.stackIN:
                self.stackOUT.append(self.stackIN.pop())

        return self.stackOUT.pop()

    def peek(self) -> int:
        if not self.stackOUT:
            while self.stackIN:
                self.stackOUT.append(self.stackIN.pop())

        return self.stackOUT[-1]

    def empty(self) -> bool:
        return not self.stackIN and not self.stackOUT


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
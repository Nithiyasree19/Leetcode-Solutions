class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val):
        m = val if not self.s else min(val, self.s[-1][1])
        self.s.append((val, m))

    def pop(self):
        self.s.pop()

    def top(self):
        return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]
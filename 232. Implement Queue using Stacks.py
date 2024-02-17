class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def _transfer_elements(self):
        if not self.stack2:
            while self.stack1:
                element = self.stack1.pop()
                self.stack2.append(element)

    def pop(self):
        self._transfer_elements()
        return self.stack2.pop()

    def peek(self):
        self._transfer_elements()
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

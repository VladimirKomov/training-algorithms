class FibonacciIterator:
    def __init__(self, max):
        self.max = max
        self.index = 0
        self.current = 0
        self.previous = 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max:
            raise StopIteration
        value = self.current
        self.current = self.previous
        self.previous = self.current + self.previous
        self.index += 1
        return value


fibonacci_iterator = FibonacciIterator(4)
for i in fibonacci_iterator:
    print(i)



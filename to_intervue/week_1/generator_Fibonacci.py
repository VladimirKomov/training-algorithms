class FibonacciGenerator:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        current = 0
        previous = 1
        count = 0
        while count < self.max:
            yield current
            current = previous
            previous = current + previous
            count += 1


def generator_function(max):
    current = 0
    previous = 1
    count = 0
    while count < max:
        yield current
        current = previous
        previous = current + previous
        count += 1

# fibonacci_generator = FibonacciGenerator(20)


# for i in generator_function(20):
#     print(i)

print(generator_function(5))

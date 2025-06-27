class Class_1:
    def print(self):
        print("From Class_1")

class Class_2(Class_1):
    def print_2(self):
        print("From Class_2")


class Class_3():
    def print_3(self):
        print("From Class_3")

class Class_4(Class_2, Class_3):
    def print_4(self):
        print("From Class_4")


my_class = Class_4()
my_class.print()
print(Class_4.__mro__)


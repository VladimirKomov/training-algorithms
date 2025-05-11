def is_armstrong_number(number):
    string_number = str(number)
    result = 0
    for digit in string_number:
        integer = int(digit)
        result += integer ** len(string_number)
    return result == number

def is_armstrong_number2(number):
    string_number = str(number)
    length = len(string_number)
    result = sum(int(digit) ** length for digit in string_number)
    return result == number

def print_result():
    numbers = [9, 10, 153, 154]
    for number in numbers:
        print(is_armstrong_number2(number))

if __name__ == '__main__':
    print_result()
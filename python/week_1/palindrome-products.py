def is_palindrome(number) -> bool:
    string_number = str(number)
    if string_number == string_number[::-1]:
        return True
    return False

def find_factors(min_factor, max_factor, palindrome):
    factors = []
    for i in range(min_factor, max_factor + 1):
        if palindrome % i == 0:
            factor = palindrome // i
            if min_factor <= factor <= max_factor:
                pair = (min(i, factor), max(i, factor))
                if pair not in factors:
                    factors.append(pair)

    return palindrome, factors


def find_min_palindrome_with_factors(min_factor, max_factor):
    for i in range(min_factor * min_factor, max_factor * max_factor + 1):
        if is_palindrome(i):
            palindrome, factors = find_factors(min_factor, max_factor, i)
            if factors:
                return palindrome, factors

    return None, []

def find_max_palindrome_with_factors(min_factor, max_factor):
    for i in range(max_factor * max_factor, min_factor * min_factor - 1, -1):
        if is_palindrome(i):
            palindrome, factors = find_factors(min_factor, max_factor, i)
            if factors:
                return palindrome, factors

    return None, []


def validation(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    validation(min_factor, max_factor)
    palindrome, factors = find_max_palindrome_with_factors(min_factor, max_factor)

    return palindrome, factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    validation(min_factor, max_factor)
    palindrome, factors = find_min_palindrome_with_factors(min_factor, max_factor)

    return palindrome, factors



def print_result():
    print(largest(1002, 1003))
    print(smallest(1002, 1003))


if __name__ == '__main__':
    print_result()
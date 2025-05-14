class PhoneNumber:
    def __init__(self, number):
        self.number = self._normalize(number)

    def _normalize(self, number_str):
        if any(c.isalpha() for c in number_str):
            raise ValueError("letters not permitted")

        digits = ''.join(c for c in number_str if c.isdigit())

        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(digits) == 11:
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        area, exchange = digits[0:3], digits[3:6]

        if area[0] == '0':
            raise ValueError("area code cannot start with zero")
        if area[0] == '1':
            raise ValueError("area code cannot start with one")
        if exchange[0] == '0':
            raise ValueError("exchange code cannot start with zero")
        if exchange[0] == '1':
            raise ValueError("exchange code cannot start with one")

        return digits

    @property
    def area_code(self):
        return self.number[0:3]

    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]})'


if __name__ == '__main__':
    p_number = PhoneNumber('+1 613-995-0253')
    print(p_number.pretty())
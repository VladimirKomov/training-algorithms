class Luhn:
    def __init__(self, card_num: str):
        self.card_num: str = card_num

    def _normalize(self) -> str:
        return self.card_num.replace(" ", "")

    def valid(self):
        digits = self._normalize()
        if len(digits) < 2 or not digits.isdigit():
            return False

        total = 0
        reversed_digits = map(int, reversed(digits))

        for inx, digit in enumerate(reversed_digits):
            if inx % 2 == 1:
                digit = digit * 2
                if digit > 9:
                    digit = digit - 9
            total += digit

        return total % 10 == 0


if __name__ == "__main__":
    l = Luhn("1")
    print(l.valid())

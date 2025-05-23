class BankAccount:
    def __init__(self):
        self._balance = 0
        self._is_open = False

    def get_balance(self):
        if not self._is_open:
            raise ValueError("account not open")
        return self._balance

    def open(self):
        if self._is_open:
            raise ValueError("account already open")
        self._is_open = True
        self._balance = 0
        return self._is_open

    def deposit(self, amount):
        if not self._is_open:
            raise ValueError("account not open")
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if not self._is_open:
            raise ValueError("account not open")
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        if amount > self._balance:
            raise ValueError("amount must be less than balance")
        self._balance -= amount
        return self._balance

    def close(self):
        if not self._is_open:
            raise ValueError("account already open")
        self._is_open = False
        return self._is_open
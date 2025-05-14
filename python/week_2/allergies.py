class Allergies:
    items = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        self.score = score
        self._allergies = [name for name, value in self.items.items() if score & value]

    def allergic_to(self, item):
        return item in self._allergies

    @property
    def lst(self):
        return self._allergies


if __name__ == "__main__":
    a = Allergies(100)
    print(a.lst)
    print(a.allergic_to("tomatoes"))

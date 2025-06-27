from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def get_data(self):
        pass

class TimeCalculator(Calculator):
    def __init__(self, time_source: str) -> None:
        self.time_source = time_source

    def get_data(self) -> str:
        return f"{self.time_source} секунд"


class TemperatureCalculator(Calculator):
    def __init__(self, temperature_source: int) -> None:
        self._temperature_source = temperature_source

    def adapt_temperature(self) -> None:
        # Нужно обязательно вызвать метод, перед тем как вызывать метод `get_data`
        self._temperature_source = str(self._temperature_source)

    def get_data(self) -> str:
        # добавляем сюда
        self.adapt_temperature()

        if not isinstance(self._temperature_source, str):
            raise TypeError("Temperature source must be a string!")
        return f"{self._temperature_source} градусов"


# Нужно выводить данные на экран
class DataPrinter:
    def print_data(self, calculator: Calculator):
        data = calculator.get_data()
        print(data)



data_printer = DataPrinter()
time_calculator = TimeCalculator(time_source="12")
# data_printer.print_data(time_calculator)

temperature_calculator = TemperatureCalculator(temperature_source=20)
data_printer.print_data(time_calculator)
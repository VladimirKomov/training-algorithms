class LightController:
    def __init__(self) -> None:
        self.is_on = False

    def turn_on(self) -> bool:
        self.is_on = True
        return self.is_on

    def turn_off(self) -> bool:
        self.is_on = False
        return self.is_on


class HeatingController:
    def __init__(self) -> None:
        self.temperature = 20

    def set_temperature(self, temperature) -> int:
        self.temperature = temperature
        return self.temperature


class AlarmController:
    def __init__(self) -> None:
        self.is_armed = False

    def activate(self) -> bool:
        self.is_armed = True
        return self.is_armed

    def deactivate(self) -> bool:
        self.is_armed = False
        return self.is_armed


class SmartHomeSystem:
    def __init__(
            self,
            light_controller: LightController,
            heating_controller: HeatingController,
            alarm_controller: AlarmController
    ) -> None:
        self.light_controller = light_controller
        self.heating_controller = heating_controller
        self.alarm_controller = alarm_controller

    def home_mode(self) -> str:
        self.light_controller.turn_on()
        self.heating_controller.set_temperature(25)
        self.alarm_controller.activate()
        return f"The temperature is {self.heating_controller.temperature} and the light is on"

    def away_mode(self) -> str:
        self.light_controller.turn_off()
        self.heating_controller.set_temperature(20)
        self.alarm_controller.deactivate()
        return f"The temperature is {self.heating_controller.temperature} and the light is off"


if __name__ == "__main__":
    smart_home = SmartHomeSystem(
        light_controller=LightController(),
        heating_controller=HeatingController(),
        alarm_controller=AlarmController()
    )

    print(smart_home.home_mode())
    print(smart_home.away_mode())

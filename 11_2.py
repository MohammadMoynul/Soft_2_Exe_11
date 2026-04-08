class Car:
    def _init_(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.km = 0

    def drive(self, hours):
        self.km += self.speed * hours


class ElectricCar(Car):
    def _init_(self, reg_number, max_speed, battery_capacity):
        super()._init_(reg_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def _init_(self, reg_number, max_speed, tank_volume):
        super()._init_(reg_number, max_speed)
        self.tank_volume = tank_volume


# main program
e_car = ElectricCar("ABC-15", 180, 52.5)
g_car = GasolineCar("ACD-123", 165, 32.3)

e_car.speed = 120
g_car.speed = 100

e_car.drive(3)
g_car.drive(3)

print("Electric car km:", e_car.km)
print("Gasoline car km:", g_car.km)

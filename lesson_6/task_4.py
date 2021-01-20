class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going')

    def show_speed(self):
        print(f'The current speed of {self.name} is {self.speed}')

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} is turning {direction}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Be careful! The speed of {self.name}is more than max.')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Be careful! The speed of {self.name} is more than max.')


class PoliceCar(Car):
    pass


town_car = TownCar(60, 'grey', 'town car', False)
sport_car = SportCar(260, 'red', 'sport car', False)
work_car = WorkCar(100, 'blue', 'work car', False)
police_car = PoliceCar(130, 'white', 'police car', True)

town_car.show_speed()
sport_car.stop()
work_car.turn('right')
police_car.show_speed()
work_car.show_speed()

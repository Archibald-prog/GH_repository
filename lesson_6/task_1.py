from time import sleep
from itertools import cycle


class TrafficLights:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 4))

    def running(self):
        for color, seconds in cycle(self.__color):
            print(color, '-', f'waiting {seconds} seconds')
            sleep(seconds)


tr_lights = TrafficLights()
tr_lights.running()

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def m_calc(self):
        return self._length * self._width * 25 * 0.05


my_road = Road(float(input('Enter the road length: ')), float(input('Enter the road width: ')))
print(my_road.m_calc())

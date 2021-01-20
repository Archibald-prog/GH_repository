class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._wages = income['wages']
        self._bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}, {self.position}:'

    def get_total_income(self):
        return self._wages + self._bonus


pos = Position('John', 'Smith', 'engineer', {'wages': 100000, 'bonus': 30000})
print(pos.get_full_name())
print(pos.get_total_income())

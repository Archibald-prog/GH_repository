import random


class Card:

    def make_card(self):
        def make_string(temp):
            nums = []
            while len(nums) < 5:
                elem = str(random.randint(1, 90))
                if elem not in temp:
                    nums.append(elem)
                    temp.append(elem)

            nums = list(nums) + list(' ' * 9)
            random.shuffle(nums)
            return ' '.join(nums)

        temp = []
        for _ in range(3):
            print(make_string(temp))


computer_card = Card()
human_card = Card()
print('Computer card')
computer_card.make_card()
print("===================================")
print('Human card')
human_card.make_card()

from random import randint


class Die():
    # define how many sides there are on a die
    def __init__(self, sides=6):
        self.sides = sides

    # time --- how many times to roll
    def roll_die(self, time=1):
        nums = ""
        while time != 0:
            num = randint(1, self.sides)
            nums += str(num) + " "
            time = time - 1
        print(nums)


die_6s = Die()
die_6s.roll_die(10)

die_10s = Die(10)
die_10s.roll_die(10)

die_20s = Die(20)
die_20s.roll_die(10)

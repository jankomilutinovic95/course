import random


class Hat:

    houses = ["Gryf", "Huff", "Raven", "Slyth"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")

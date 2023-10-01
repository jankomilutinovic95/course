students = [
    {'name': 'Hermione', 'house': 'Gryff'},
    {'name': 'Harry', 'house': 'Gryff'},
    {'name': 'Ron', 'house': 'Gryff'},
    {'name': 'Draco', 'house': 'Slyth'},
    {'name': 'Padma', 'house': 'Raven'},
]

houses = set()
for student in students:
    houses.add(student['house'])

for house in sorted(houses):
    print(house)

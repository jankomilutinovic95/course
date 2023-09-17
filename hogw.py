students = [
    {"name": "Herm", "house": "Gryf", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryf", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryf", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slyth", "patronus": None}
            ]

for i, student in enumerate(students, start=1):
    print(i, student["name"], student["house"], student["patronus"], sep=", ")

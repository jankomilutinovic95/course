age = int(input("Age? "))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16, 66):
    print("have a good day at work")
else:
    print("free time")

print("-" * 80)

if age < 16 or age > 65:
    print("free time")
else:
    print("have a good day at work")

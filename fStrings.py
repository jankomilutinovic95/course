for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)
name = input("enter name: ")
age = int(input("how old are you, {0}?".format(name)))
print(age)
if age >= 18:
    print("vote")
elif age == 900:
    print("fosil")
else:
    print("no")

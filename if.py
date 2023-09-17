answer = 5

print("Guess a number between 1 and 10: ")
guess = int(input())

# if guess != answer:
#     if guess < answer:
#         print("guess higher")
#     else:
#         print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("you guessed")
#     else:
#         print("still not correct")
# else:
#     print("you guessed it first time")

if guess == answer:
    print("you guessed it first time")
else:
    if guess < answer:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input())
    if guess == answer:
        print("you guessed it")
    else:
        print("still not correct")


# if guess < answer:
#     print("guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("well done")
#     else:
#         print("bad guess again")
# elif guess > answer:
#     print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done")
#     else:
#         print("bad guess again")
# else:
#     print("correct")


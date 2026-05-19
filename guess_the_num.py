import random
secret_num = random.randint(1,100)

attempt = 0

while attempt <= 5:

    user_guess = int(input("guess the secret number: "))

    if user_guess > secret_num:
        print("too high!")
    elif user_guess < secret_num:
        print("too low!")
    else:
        print("spot on!")

    attempt += 1
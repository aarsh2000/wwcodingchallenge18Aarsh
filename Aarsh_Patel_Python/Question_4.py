import random


attempt = 3
taken_numbers = []
random_number = random.randint(1, 20)
while attempt > 0:
    guess_number = int(input(("Attempt: "+str(attempt)+ (" Guess a number between 1-20: "))))
    if guess_number == random_number:
        print("Your Guess was right")
        attempt = 0
    elif guess_number > random_number:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    for i in taken_numbers:
        if guess_number == i:
            attempt += 1
    taken_numbers.append(guess_number)
    attempt -= 1

print("The number was " + str(random_number))
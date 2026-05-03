import random
secret_number = random.randint(1,100)
attempts = 0
max_attempts = 7
while attempts < max_attempts:
    attempts += 1
    user_input = int(input("Enter a number: "))
    if user_input < secret_number:
        print("Too Low")
    elif user_input > secret_number:
        print("Too High")
    else:
        print(f"You got it! You won in {attempts} attempts.")
        break
else:
    print(f"Out of attempts. The number was {secret_number}.")
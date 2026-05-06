import random

def get_user_guess():
    user_input = int(input("Enter a number: "))
    return  user_input

def check_user_guess(guess,secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"

def is_valid_guess(my_guess,low,high):
    return low <= my_guess <= high

secret_number = random.randint(1,100)
attempts = 0
max_attempts = 7
while attempts < max_attempts:
    guess = get_user_guess()
    if not is_valid_guess(guess,1,100):
        print("Out of Range. Try again")
        continue
    attempts += 1
    result = check_user_guess(guess,secret_number)
    if result == "low":
        print("Too Low")
    elif result == "high":
        print("Too High")
    else:
        print(f"Correct. You got it in {attempts} attempts")
        break
else:
    print(f"Out of attempts. The number was {secret_number}.")






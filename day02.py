user_name = input("What's your name?:").upper()
birth_year = int(input("What's your birth year?:"))
user_age = 2026 - birth_year
fav_word = input("What's your favorite word?:")
length_word = len(fav_word)
reversed_word = fav_word[::-1]
print(f"{user_name}\n{user_age}\n{length_word}\n{reversed_word}")
if user_age % 2 == 0:
    print("Age is even")
else:
    print("Age is odd")
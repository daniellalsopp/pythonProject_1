secret = 6

guess = int(input("Take a guess at the secret number:"))

if guess == "6":
    print("Correctamundo!")

else:
    print("Sorry, the secret number is actually" , str(secret))


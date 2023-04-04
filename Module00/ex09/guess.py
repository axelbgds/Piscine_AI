import sys, random

tryNb = 0
answer = random.randint(1, 99)

print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
''')

while True:
	guess = input("What's your guess between 1 and 99?\n")
	tryNb += 1
	if guess == "exit":
		sys.exit("Looser~")
	if guess.isdigit() == False:
		print("That's not a number.")
	elif int(guess) != answer:
		print("Too high!" if int(guess) > answer else "Too low!")
	else:
		if answer == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		sys.exit("Congratulations! You got it on your first try!" if tryNb == 1 
			else "Congratulations, you've got it! You won in {} attempts!".format(tryNb))

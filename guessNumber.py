import random
secretNum=random.randint(1,20)
print("I am thinking number is between 1 to 20.")

for guessess in range(5):
    print("Take a guess.")
    guess=int(input())
    
    if guess< secretNum:
        print("Your guess is too low.")
    elif guess> secretNum:
        print("You are too high.")
    else:
        break
if guess==secretNum:
    print("Good job! you guessed my number in",str(guessess + 1),'guesses!')            
else:
    print('Nope. The number I was thinkig of was ',secretNum,"." )   
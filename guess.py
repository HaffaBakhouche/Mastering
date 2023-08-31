import math
import random as rand

def GuessNumber():
    a = int(input("Entrez votre chiffre a: "))
    b = int(input("Entre votre chiffre B: "))
    RandomNumToGuess = rand.randint(a,b)
    tentatives = 0
    guess = 0

    while RandomNumToGuess != guess:
            guess = int(input("Entrez votre chiffre: "))
            tentatives+= 1
            if RandomNumToGuess == guess:
                print("\nCongratz, you won in",tentatives,"tentatives")
                print("\nThe Guessed number was",guess,'.')
                break
            elif RandomNumToGuess < guess:
                print("\nPlus bas.. ")
            elif RandomNumToGuess > guess:
                print("\nPlus haut ..")

GuessNumber()
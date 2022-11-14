import random

Hangman = [
    """
-----
|   |
|  
| 
|   
|  
| 
| 
|
--------
""",
    """
-----
|   |
|   0
| 
|   
|  
| 
| 
|
--------
""",
    """
-----
|   |
|   0
| |-_-|
|  
|  
| 
| 
|
--------
""",
    """
-----
|   |
|   0
| |-_-|
|   |
|   
| 
| 
|
--------
""",
    """
-----
|   |
|   0
| |-_-|
|   |
|   |
| 
| 
|
--------
""",
    """
-----
|   |
|   0
| |-_-|
|   |
|   |
| | . |
| 
|
--------
""",
    """
-----
|   |
|   0
| |-_-|
|   |
|   |
| | . |
| |   |
|
--------
""",
]

word_list = ["python", "nsst", "class", "list", "tuples", "project", "dictionary"]
word = list(random.choice(word_list))

display = []

guessed_letters = []

display.extend(word)
guessed_letters.extend(display)
for i in range(len(display)):
    display[i] = "_"
print(" ".join(display))
print()
print("Total letters : ", len(display))
print()

life = len(Hangman) -1

while list.count(display, "_") > 0 and life != 0:
    guess = input("Guess a letter please : ")
    guess = guess.lower()

    if guess == "".join(word):
        display = list(guess)
        print("\n Yay! you scored all letters!")
        print(" ".join(display))
        break

    for i in range(len(word)):
        if word[i] == guess and guess in guessed_letters:
            display[i] = guess
            guessed_letters.remove(guess)
    if guess not in display:
        print("Sorry this letter is wrong ")
        life -= 1
    print(Hangman[(len(Hangman)-1)-life])
    print(" ".join(display))
    print()

print("Game Over!")

import random
import time
import colorama
from colorama import Fore

# function that removes the non-alphabetic characters from the user's input
def removeExtra(word):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    new_word = ""
    for i in range(len(word)):
        if word[i].lower() in alphabet:
            new_word += word[i]
    return new_word

# function that displays the structure with the lava level
def displayStructure(player, structure, level):
    if level >= len(structure):
        spaces = " " * (level-len(structure))
        print("Player " + str(player) + ": " + structure + spaces + Fore.RED + "|" + Fore.LIGHTWHITE_EX)
    else:
        print("Player " + str(player) + ": " + structure[0:level] + Fore.RED + "|" + Fore.LIGHTWHITE_EX + structure[level:])

lava_level = 0
increment = 1
done = False
player1_words = ""
player2_words = ""
winner = None
round = 1
last_index = -1

print("\n")
print(Fore.LIGHTWHITE_EX + "This is a two player game where both players compete to choose a longer word based on the given category. \nAfter both players enter their word their stuctures will rise based on the length of the words. \nLava will then rise and the first player that the lava overtakes loses.")
print("\nLet's begin!\n\n")
time.sleep(0.5)
categories = ["Instruments", "Family Members", "Professions", "Articles of Clothing", "Months", "Sports", "School Subjects", "Colors of the Rainbow", "Days of the Week", "Planets in the Solar System"]

# game loop
while not done:
    # select random category
    index = random.randrange(0, 10)
    # generate index until not a repeat of last round
    while index == last_index:
        index = random.randrange(0, 10)
    last_index = index
    with open(categories[index], "r") as file:
        selected_category = file.readlines()
    selected_category = [line.strip() for line in selected_category]

    print("Round " + str(round))
    print()

    print("Category: " + categories[index])
    print()

    # take player 1's input and remove's extra characters
    word1 = removeExtra(input("Player 1 enter your word: "))

    # if word is in category, add to structure
    if word1.lower() in selected_category:
        player1_words += word1.lower()

    # if not in category, prompt player 1 max 4 more times
    else:
        for i in range(4):
            word1 = removeExtra(input("That word is not in the category. Try Again: "))
            if word1 in selected_category:
                player1_words += word1
                break
            if i == 3:
                print("Sorry, you have run out of attempts.")

    # take player 2's input and remove's extra characters
    word2 = removeExtra(input("Player 2 enter your word: "))

    # if word is in category, add to structure
    if word2.lower() in selected_category:
        player2_words += word2.lower()

    # if not in category, prompt player 2 max 4 more times
    else:
        for i in range(4):
            word2 = removeExtra(input("That word is not in the category. Try Again: "))
            if word2 in selected_category:
                player2_words += word2
                break
            if i == 3:
                print("Sorry, you have run out of attempts.")

    print()

    # raise lava level
    lava_level += increment

    print("Raising lava by " + str(increment) + "...")
    print()
    time.sleep(0.5)

    # increase amount added to lava
    increment += 3

    # display structures with lava level of both players
    displayStructure(1, player1_words, lava_level)
    displayStructure(2, player2_words, lava_level)
    print()

    time.sleep(0.5)

    # if lava has overtaken both players -> nobody wins, end game
    if lava_level >= len(player1_words) and lava_level >= len(player2_words):
        winner = "Nobody"
        done = True
    # else if lava has overtaken both player 1 -> player 2 wins, end game
    elif lava_level >= len(player1_words):
        winner = "Player 2"
        done = True
    # else if lava has overtaken both player 2 -> player 1 wins, end game
    elif lava_level >= len(player2_words):
        winner = "Player 1"
        done = True

    # update round
    round += 1
    print()

# display winner
print("Winner: " + winner)
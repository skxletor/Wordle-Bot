import itertools
import os
import sys
import traceback

def _pause_on_error(exc_type, exc_value, exc_tb):
    traceback.print_exception(exc_type, exc_value, exc_tb)
    input("\nAn error occurred. Press Enter to close...")

sys.excepthook = _pause_on_error

knownLetters = []
greyLetters = []



greyLettersv = input('Enter the letters that are grey as one word (ex: abcd): ')

greyLetters = list(greyLettersv)

#print(greyLetters)

w1 = w2 = w3 = w4 = w5 = '_'

while True:
   
   
    slotAsk = input('Which slot would you like to input a letter for? (1-5), or if you are done, type "done": ')
    
    if slotAsk == 'done':
        break
    
     #code for first slot 

    if slotAsk == '1':
        ask1 = input('Enter the letter you entered in the first slot: ')
        if ask1 in greyLetters:
            print('Invalid input. Please try again.')
            continue

        gORy = input('Is the letter green or yellow? (g or y) ')
        if gORy == 'g':
            knownLetters.append(ask1)
            w1 = ask1
        elif gORy == 'y':
            knownLetters.append(ask1)
            w1 != ask1
        else:
            print('Invalid input. Please try again.')
            continue
         
    #code for second slot 

    if slotAsk == '2':
        ask2 = input('Enter the letter you entered in the second slot: ')
        if ask2 in greyLetters:
            print('Invalid input. Please try again.')
            continue

        gORy = input('Is the letter green or yellow? ')
        if gORy == 'green':
            knownLetters.append(ask2)
            w2 = ask2
        elif gORy == 'yellow':
            knownLetters.append(ask2)
            w2 != ask2
        else:
            print('Invalid input. Please try again.')
            continue
  
    #code for third slot 

    if slotAsk == '3':
        ask3 = input('Enter the letter you entered in the third slot: ')
        if ask3 in greyLetters:
            print('Invalid input. Please try again.')
            continue

        gORy = input('Is the letter green or yellow? ')
        if gORy == 'green' and ask3 not in greyLetters:
            knownLetters.append(ask3)
            w3 = ask3
        elif gORy == 'yellow' and ask3 not in greyLetters:
            knownLetters.append(ask3)
            w3 != ask3
        else:
            print('Invalid input. Please try again.')
            continue
   
    #code for fourth slot 

    if slotAsk == '4':
        ask4 = input('Enter the letter you entered in the fourth slot: ')
        if ask4 in greyLetters:
            print('Invalid input. Please try again.')
            continue

        gORy = input('Is the letter green or yellow? ')
        if gORy == 'green' and ask4 not in greyLetters:
            knownLetters.append(ask4)
            w4 = ask4
        elif gORy == 'yellow' and ask4 not in greyLetters:
            knownLetters.append(ask4)
            w4 != ask4
        else:
            print('Invalid input. Please try again.')
            continue

    #code for fifth slot 

    if slotAsk == '5':
        ask5 = input('Enter the letter you entered in the fifth slot: ')
        if ask5 in greyLetters:
            print('Invalid input. Please try again.')
            continue
        gORy = input('Is the letter green or yellow? ')
        if gORy == 'green' and ask5 not in greyLetters:
            knownLetters.append(ask5)
            w5 = ask5
        elif gORy == 'yellow' and ask5 not in greyLetters:
            knownLetters.append(ask5)
            w5 != ask5
        else:
            print('Invalid input. Please try again.')
            continue
    word = [w1, w2, w3, w4, w5]








# Load the list of valid words from a file
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionaryWordle.txt'), 'r', encoding='utf-8') as file:
    valid_words = set(file.read().split())

# Generate all possible combinations
alphabet = [chr(i) for i in range(97, 123)]  # List of all lowercase letters
valid_letters = [letter for letter in alphabet if letter not in greyLetters]

# Replace '_' with valid letters
slots = [valid_letters if letter == '_' else [letter] for letter in word]

# Generate and print all combinations that include all known letters and are valid words
for combination in itertools.product(*slots):
    combination_str = ''.join(combination)
    if all(letter in combination_str for letter in knownLetters) and combination_str in valid_words:
        print(combination_str)

print("Known letters:", knownLetters)

input("press enter to leave")
print('Goodbye!')



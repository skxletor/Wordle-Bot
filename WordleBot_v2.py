import itertools
import os
import sys
import traceback
import requests
from bs4 import BeautifulSoup

def _pause_on_error(exc_type, exc_value, exc_tb):
    traceback.print_exception(exc_type, exc_value, exc_tb)
    input("\nAn error occurred. Press Enter to close...")

sys.excepthook = _pause_on_error

knownLetters = []
greyLetters = []

greyLettersv = input('Enter the letters that are grey as one word (ex: abcd): ')
greyLetters = list(greyLettersv)

w = ['_', '_', '_', '_', '_']

def slotAsk(slotNum):
    while True:
        ask = input(f'Enter the letter you entered in slot {slotNum}: ')
        if ask in greyLetters:
            print('Invalid input. Please try again.')
            continue
        if len(ask)!=1:
            print('Invalid input. Please try again.')
            continue

        gORy = input('Is the letter green or yellow? (g or y) ')
        if gORy == 'g':
            knownLetters.append(ask)
            w[slotNum - 1] = ask
            break
        elif gORy == 'y':
            knownLetters.append(ask)
            break
        else:
            print('Invalid input. Please try again.')

while True:
    slot_input = input('Which slot would you like to input a letter for? (1-5), or if you are done, type "done": ')

    if slot_input == 'done':
        break

    if slot_input in ('1', '2', '3', '4', '5'):
        slotAsk(int(slot_input))
    else:
        print('Invalid input. Please enter 1-5 or "done".')


# Load the list of valid words from a file
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionaryWordle.txt'), 'r', encoding='utf-8') as file:
    valid_words = set(file.read().split())

# Generate all possible combinations
alphabet = [chr(i) for i in range(97, 123)]  # List of all lowercase letters
valid_letters = [letter for letter in alphabet if letter not in greyLetters]

# Replace '_' with valid letters
slots = [valid_letters if letter == '_' else [letter] for letter in w]

# Fetch past Wordle answers to exclude
past_answers = set()
try:
    response = requests.get('https://www.rockpapershotgun.com/wordle-past-answers', timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find('ul', class_='inline')
    if ul:
        for li in ul.find_all('li'):
            word = li.get_text(strip=True).lower()
            if len(word) == 5:
                past_answers.add(word)
except Exception:
    print("Warning: Could not fetch past answers. No words will be excluded.")

# Generate and print all combinations that include all known letters and are valid words
for combination in itertools.product(*slots):
    combination_str = ''.join(combination)
    if all(letter in combination_str for letter in knownLetters) and combination_str in valid_words and combination_str not in past_answers:
        print(combination_str)

# print("Known letters:", knownLetters)

input("press enter to leave")
print('bye')

import itertools

knownLetters = []
greyLetters = []
yellowLetters = {}

greyLettersv = input('Enter the letters that are grey as one word (ex: abcd): ')

greyLetters = list(greyLettersv)

#print(greyLetters)

w1 = w2 = w3 = w4 = w5 = '_'

while True:
    slotAsk = input('Which slot would you like to input a letter for? (1-5), or if you are done, type "done": ')
    
    if slotAsk == 'done':
        break
    
    if slotAsk == '1':
        ask1 = input('Enter the letter you entered in the first slot: ')
        if ask1 in greyLetters:
            print('Invalid input. Please try again.')
            continue

        gORy = input('Is the letter green or yellow? ')
        if gORy == 'green':
            knownLetters.append(ask1)
            w1 = ask1
        elif gORy == 'yellow':
            knownLetters.append(ask1)
            yellowLetters[1] = ask1
        else:
            print('Invalid input. Please try again.')
            continue
         
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
            yellowLetters[2] = ask2
        else:
            print('Invalid input. Please try again.')
            continue
  
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
            yellowLetters[3] = ask3
        else:
            print('Invalid input. Please try again.')
            continue
   
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
            yellowLetters[4] = ask4
        else:
            print('Invalid input. Please try again.')
            continue

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
            yellowLetters[5] = ask5
        else:
            print('Invalid input. Please try again.')
            continue

word = [w1, w2, w3, w4, w5]

# Generate all possible combinations
alphabet = [chr(i) for i in range(97, 123)]  # List of all lowercase letters
valid_letters = [letter for letter in alphabet if letter not in greyLetters]

# Replace '_' with valid letters, ensuring yellow letters are not in their original positions
slots = []
for i, letter in enumerate(word):
    if letter == '_':
        valid_slot_letters = [l for l in valid_letters if yellowLetters.get(i + 1) != l]
        slots.append(valid_slot_letters)
    else:
        slots.append([letter])

# Generate and print all combinations that include all known letters
for combination in itertools.product(*slots):
    combination_str = ''.join(combination)
    if all(letter in combination_str for letter in knownLetters):
        print(combination_str)

print("Known letters:", knownLetters)

final = input('Say when done:')
if final == 'done':
    print('Goodbye!')
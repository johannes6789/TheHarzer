import random
from itertools import cycle

dice1 = [1, 2, 3, 4, 5, 6]
answer = 'whatever'
currentRoll = ''
player_names = []
list1 = iter(player_names)
Player = ''
allPlayers: dict = {}
dice_roll_count = 0

number_of_players = ' '
n = number_of_players

imHarzer = {'Harzer1': 0, 'Harzer2': 0, 'Harzer3': 0, 'Harzer4': 0,
            'Harzer5': 0, 'Harzer6': 0, 'Summe:': 0}

while True:
    try:
        number_of_players = int(input('how many Players?'))
    except:
        print('Please enter a number!')
    else:
        print('Thank you!')
        break

while True:
    try:
        number_of_sticks = int(input('how many Sticks?'))
    except:
        print('Please enter a number!')
    else:
        print('Thank you!')
        break

for x in range(1, number_of_players + 1):
    allPlayers[input('Player ' + str(x) + ', what is your name?')] = int(number_of_sticks)

for n in allPlayers.keys():
    player_names.append(str(n))


def taken_spot():
    for i in imHarzer.keys():
        if imHarzer[i] == 2:
            return 'True'
    else:
        return 'False'


def winning():
    for value in allPlayers.values():
        if value == 0:
            return 'True'
        else:
            return 'False'


keys = allPlayers.keys()
all_players_keys = cycle(iter(keys))


def next_player():
    for i in cycle(all_players_keys):
        yield i


g = next_player()

while winning() != 'True':

    dice_roll_count = 0
    Player = next(g)

    while True:

        print(Player + ' its your turn!')
        print(f'The Current Situation is: {imHarzer} ')
        answer = input('Do you want to roll the dice?')
        currentRoll = str(random.choice(dice1))
        if answer == 'no' and dice_roll_count == 0:
            print('You have to roll the dice at least once!!!')
            continue

        elif answer == 'no':

            imHarzer['Harzer6'] = 0
            imHarzer['Summe:'] = sum(int(val) for key, val in imHarzer.items() if key != 'Summe:')
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break
            break

        if currentRoll == '1':
            imHarzer["Harzer1"] += 1
            allPlayers[Player] -= 1
            dice_roll_count += 1
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break

        if currentRoll == '2':
            imHarzer["Harzer2"] += 1
            allPlayers[Player] -= 1
            dice_roll_count += 1
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break

        if currentRoll == '3':
            imHarzer["Harzer3"] += 1
            allPlayers[Player] -= 1
            dice_roll_count += 1
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break

        if currentRoll == '4':
            imHarzer["Harzer4"] += 1
            allPlayers[Player] -= 1
            dice_roll_count += 1
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break

        if currentRoll == '5':
            imHarzer["Harzer5"] += 1
            allPlayers[Player] -= 1
            dice_roll_count += 1
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break

        if currentRoll == '6':
            imHarzer["Harzer6"] += 1
            allPlayers[Player] -= 1
            dice_roll_count += 1
            if winning() == 'True':
                print('Congratulations, ' + Player + ' you won !!!')
                break

        imHarzer['Summe:'] = sum(int(val) for key, val in imHarzer.items() if key != 'Summe:')

        print('you rolled a ' + currentRoll + '!')

        if taken_spot() == 'True':

            allPlayers[Player] += ((imHarzer['Summe:']) - (imHarzer['Harzer6']))
            imHarzer['Harzer1'] = 0
            imHarzer['Harzer2'] = 0
            imHarzer['Harzer3'] = 0
            imHarzer['Harzer4'] = 0
            imHarzer['Harzer5'] = 0
            imHarzer['Harzer6'] = 0
            imHarzer['Summe:'] = sum(int(val) for key, val in imHarzer.items() if key != 'Summe:')
            break

    print('its over!')
    print(allPlayers)

print(allPlayers, imHarzer)
print(allPlayers.items())
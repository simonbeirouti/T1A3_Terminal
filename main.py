# import os
import random
from time import sleep
from rich.console import Console
from functions import *
console = Console()

player = []
opponent = []

wager = 0
player_balance = 10
opponent_balance = 10

continue_game = True
o_card_val = 0
p_card_val = 0
winner = ''

player_tally = 0
opponent_tally = 0

file = open('./files/cards.txt', 'r')
deck = file.read().splitlines()

def ask_wager():
    global wager
    wager = int(input('To play, you will need to choose a wager.\n\nChoose 1, 2 or 3: '))
    if wager == 1:
        wager = 1
        console.print('\n\nThat\'s a bit cheap.. But okay.\n\nLet\'s goooo!')
    elif wager == 2:
        wager = 2
        console.print('\nThat\'s a fair wager. I like it.\n\nLet\'s goooo!')
    elif wager == 3:
        console.print('\nWhat are we waiting for! Let\'s gamble!\n\nLet\'s goooo!')
        wager = 3
    else:
        console.print(f'\nNot a valid number. Defaulting to a wager of 2.\n\nLet\'s goooo!')
        wager = 2

def player_cards():
    i = random.randint(0,len(deck) -1)
    player.append(deck[i])
    return player

def opponent_cards():
    i = random.randint(0,len(deck) -1)
    opponent.append(deck[i])
    return opponent

def player_card_value():
    global p_card_val
    for i in range(0,2):
        if player[i][0] == 'A':
            p_card_val += 11
        elif player[i][0] == 'K' or player[i][0] == 'Q' or player[i][0] == 'J' or player[i][0] == '1':
            p_card_val += 10
        else:
            p_card_val += int(player[i][0])
    return p_card_val

def opponent_card_value():
    global o_card_val
    for i in range(0,2):
        if opponent[i][0] == 'A':
            o_card_val += 11
        elif opponent[i][0] == 'K' or opponent[i][0] == 'Q' or opponent[i][0] == 'J' or opponent[i][0] == '1':
            o_card_val += 10
        else:
            o_card_val += int(opponent[i][0])
    return o_card_val

def point_check():
    os.system('clear')
    global winner, player_balance, opponent_balance, player_tally, opponent_tally
    if p_card_val > o_card_val:
        winner = 'Player'
        player_balance += wager
        opponent_balance -= wager
        player_tally += 1
        console.print(f'\nYou won! You now have {player_balance} chips.\n', style='green')
    elif p_card_val < o_card_val:
        winner = 'Opponent'
        opponent_balance += wager
        player_balance -= wager
        opponent_tally += 1
        console.print(f'\nYou lost! You now have {player_balance} chips.\n', style='red')
    else:
        winner = 'Draw'
        console.print('\nIt\'s a draw!\n')
    return winner

def game_flow():
    for i in range(0, 4):
        if i == 1 or i == 2:
            player_cards()
        else:
            opponent_cards()

    player_card_value()
    opponent_card_value()
    point_check()
    p = ' '.join(player)
    o = ' '.join(opponent)
    results_table(p, o, winner, player_tally, opponent_tally)

def choice_check():
    global continue_game
    choice = input('\nWould you like to play again?\nY for Yes\nQ for No\n')
    choice.lower()
    if choice == 'y':
        continue_game = True
    elif choice == 'q':
        exit()
    else:
        console.print('\nNot a valid choice.\n')
        exit()

def balance_checker():
    if player_balance == 0:
        os.system('clear')
        console.print('\nNo more funds. Send bitcoin here:\n\nbc1qpv8cfxsmw4j7sjd3rvh9lucwk2al6pw6cwzu43\n')
        opponent_tally += 1
        exit()
    elif opponent_balance == 0:
        os.system('clear')
        console.print('\nThe opponent has no chips left!\n\nYou win!\n')
        exit()
    else:
        pass

def main():
    introduction()
    ask_wager()
    sleep(2)

    while continue_game:
        global player, opponent, p_card_val, o_card_val, winner
        player = []
        opponent = []
        o_card_val = 0
        p_card_val = 0
        winner = ''
        game_flow()
        choice_check()
        balance_checker()

main()
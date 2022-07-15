import os
import random
from rich.console import Console
from functions import *
from rich.traceback import install
install()

os.system('clear')
console = Console(record=True)

# total_cards = []
burnt_cards = []
player = []
opponent = []
community = []
wager = 0

file = open('./files/cards.txt', 'r')
cards = file.read().splitlines()
total_cards = cards

def deal_card(i):
    cards[i] = random.choice(cards)
    return cards[i]

def player_cards(i):
    player.append(deal_card(i))
    total_cards.remove(deal_card(i))
    return player

def opponent_cards(i):
    opponent.append(deal_card(i))
    total_cards.remove(deal_card(i))
    return opponent

def burn_card(i):
    burnt_cards.append(deal_card(i))
    total_cards.remove(deal_card(i))
    return burnt_cards

def board_cards(i):
    community.append(deal_card(i))
    total_cards.remove(deal_card(i))
    return community


for i in range(0, 12):
    if i == 1 or i == 2:
        player_cards(i)
    elif i == 3 or i == 4:
        opponent_cards(i)
    elif i == 5 or i == 9 or i == 11:
        burn_card(i)
    else:
        board_cards(i)

introduction()
ask_wager()
for i in range(0, 10):
    results_table(player, community, opponent)
    sleep(2)
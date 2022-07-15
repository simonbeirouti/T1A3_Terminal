import os
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from time import sleep
console = Console()

def sleep_clear():
    sleep(1)
    os.system('clear')

MARKDOWN = """
# Welcome to the World Terminal of Poker!
"""

def introduction():
    console.print(Markdown(MARKDOWN))
    console.print('This is a game of chance. I wish you luck!\n')

def ask_wager():
    global wager
    wager = int(input('What wager do you want?\nChoose 1, 2 or 3: '))
    if wager == 1:
        wager = 1
        console.print('That\'s a bit cheap.. But okay.')
    elif wager == 2:
        wager = 2
        console.print('That\'s a fair wager. I like it.')
    elif wager == 3:
        wager = 3
        console.print('What are we waiting for! Let\'s gamble!')
    else:
        wager = 2
        console.print('You entered an invalid wager. Defaulting to a wager of 2.')
    return wager

def results_table(player, community, opponent):
    table = Table(title="Flips for lolz")

    table.add_column("Players Cards", justify="left", style="cyan")
    table.add_column("Board", justify="center", style="magenta")
    table.add_column("Opponents Cards", justify="right", style="cyan")

    table.add_row(f"{player}", f"{community}", f"{opponent}")
    with open('./files/results.txt', 'a') as f:
        f.write(f"\nPlayers cards: {player}")
        f.write(f"\nOpponents cards: {opponent}")
        f.write(f"\nCommunity cards:{community}\n")
    console.print(table)
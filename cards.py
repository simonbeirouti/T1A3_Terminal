import os
import time
from rich.console import Console
from rich.progress import Progress
from functions import introduction

cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
suits = ('♠️', '♦️', '♣️', '❤️')

total_cards = []

console = Console()
os.system('clear')

introduction('I will now create a deck of cards.\n')

console.print('\n:robot: I am the card master...\n')

with Progress() as progress:
    task = progress.add_task("[green]Creating a new deck of cards...", total=52)

    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.05)

with open('./files/cards.txt', 'w+') as f:
    for i in cards:
        for j in suits:
            f.write(i + j + '\n')
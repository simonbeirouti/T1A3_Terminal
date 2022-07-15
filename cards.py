import os
import time
from rich.console import Console
from rich.progress import Progress

cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
suits = ('S', 'D', 'H', 'C')

total_cards = []

console = Console()
os.system('clear')

console.print('\n:robot: I am the card master...\n')

with Progress() as progress:
    task = progress.add_task("[green]Creating a new deck of cards...", total=52)

    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.05)

with open('./files/cards.txt', 'w+') as f:
    for i in range(len(cards)):
        for j in range(len(suits)):
            f.write(cards[i] + suits[j] + '\n')
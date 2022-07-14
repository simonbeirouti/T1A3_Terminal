import time
from rich.console import Console
from rich.progress import Progress

console = Console()

with Progress() as progress:
    task = progress.add_task("[red]Scanning the deck of cards...\n", total=1000)

    while not progress.finished:
        progress.update(task, advance=100)
        time.sleep(0.1)

def count_cards():
    with open('./files/cards.txt', 'r') as f:
        lines = sum(1 for line in f)
    return lines

if count_cards() == 52:
    console.print('There are 52 cards in this deck.\nLet\'s start the game!')
else:
    console.print('Someone is tampering with the deck of cards.\nDo not play.')
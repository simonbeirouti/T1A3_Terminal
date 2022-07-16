import os
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
console = Console()

MARKDOWN = """
# Welcome to the World Terminal of Poker!
"""

def introduction():
    os.system('clear')
    console.print(Markdown(MARKDOWN))
    console.print('This is a game of chance. I wish you luck!\n')

def results_table(player, opponent, winner):
    table = Table(title="Flips")

    table.add_column("Players", justify="center", style="cyan")
    table.add_column("Opponents", justify="center", style="cyan")
    table.add_column("Winner", justify="center", style="magenta")

    table.add_row(f"{player}", f"{opponent}", f"{winner}")
    
    with open('./files/results.txt', 'a') as f:
        f.write(f"\nPlayers cards: {player}")
        f.write(f"\nOpponents cards: {opponent}")
        f.write(f"\nWinner: {winner}\n")
    console.print(table)
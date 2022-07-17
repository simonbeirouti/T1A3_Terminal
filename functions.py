import os
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
console = Console()

GAMETITLE = """
# World Terminal of Poker!
"""

FLIPS = """
# Time for some flips!
"""

RESULTS = """
# Time for some flips!
"""

def introduction(i):
    os.system('clear')
    if i == 'gane':
        console.print(Markdown(GAMETITLE))
    elif i == 'flips':
        console.print(Markdown(FLIPS))
    else:
        console.print(Markdown(RESULTS))

def results_table(player, opponent, winner, player_tally, opponent_tally):
    table = Table(title="Flips")

    table.add_column("Players", justify="center", style="cyan bold")
    table.add_column("Opponents", justify="center", style="cyan bold")
    table.add_column("Winner", justify="center", style="magenta bold")
    table.add_column("Player wins", justify="center", style="blue bold")
    table.add_column("Opponent wins", justify="center", style="blue bold")

    table.add_row(f"{player}", f"{opponent}", f"{winner}", f"{player_tally}", f"{opponent_tally}")
    
    with open('./files/results.txt', 'a') as f:
        f.write(f"\nPlayers cards: {player}")
        f.write(f"\nOpponents cards: {opponent}")
        f.write(f"\nWinner: {winner}")
        f.write(f"\nPlayer wins: {player_tally}")
        f.write(f"\nOpponent wins: {opponent_tally}\n")
    console.print(table)
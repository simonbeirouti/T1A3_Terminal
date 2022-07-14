from rich.console import Console
from rich.table import Table
console = Console()

def ask_wager():
    wager = int(input('What wager do you want?\nChoose 1, 2 or 3.\n'))
    if wager == 1:
        console.print('That\s a bit cheap.. But okay.')
    elif wager == 2:
        console.print('That\s a fair wager. I like it.')
    elif wager == 3:
        console.print('What are waiting for! Let\s gamble!')
    else:
        console.print('You entered an invalid wager. Defaulting to a wager of 2.')
    return wager

def results_table(player, community, opponent):
    table = Table(title="Flips for lolz")

    table.add_column("Players Cards", justify="left", style="cyan")
    table.add_column("Board", justify="center", style="magenta")
    table.add_column("Opponents Cards", justify="right", style="cyan")

    table.add_row(f"{player}", f"{community}", f"{opponent}")
    with open('results.txt', 'a') as f:
        f.write(f"\nPlayers cards: {player}")
        f.write(f"\nOpponents cards: {opponent}")
        f.write(f"\nCommunity cards:{community}\n")
    console.print(table)
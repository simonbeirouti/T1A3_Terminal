from rich.console import Console
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
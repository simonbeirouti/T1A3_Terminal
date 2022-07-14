import os
import random
from rich.console import Console
from rich.table import Table

os.system('clear')
console = Console(record=True)

total_cards = []
burnt_cards = []
player_dealt_card = []
opponent_dealt_card = []
import time
import random

ITEMS_COLLECTION = ["\U0001F352", "\U0001F349", "\U0001F347", "\U0001F34B", "\U0001F6E1", "\U0001F48E", "\U0001F4B2", "\U0001F514", "\U0001F34A", "\U00002764", "\U0001F34C", "7", "\U0001F34E", "\U0001F340"]
# ['🍒', '🍉', '🍇', '🍋', '🛡', '💎', '💲', '🔔', '🍊', '❤', '🍌', '7', '🍎', '🍀']

ACTUAL_MONEY_LEFT_EMOJI = ["\U0001F4B5"]

actual_money = 0
free_shots = 0

choose1 = random.choice(ITEMS_COLLECTION)
choose2 = random.choice(ITEMS_COLLECTION)
choose3 = random.choice(ITEMS_COLLECTION)

print(choose1, end=" "); time.sleep(0.5); print(choose2, end=" "); time.sleep(0.5); print(choose3, end=" ")
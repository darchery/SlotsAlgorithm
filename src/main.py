import time
import random

ITEMS_COLLECTION = ["\U0001F352", "\U0001F349", "\U0001F347", "\U0001F34B", "\U0001F6E1", "\U0001F48E", "\U0001F4B2", "\U0001F514", "\U0001F34A", "\U00002764", "\U0001F34C", "\U00000037", "\U0001F34E", "\U0001F340"]
# ['🍒', '🍉', '🍇', '🍋', '🛡', '💎', '💲', '🔔', '🍊', '❤', '🍌', '7', '🍎', '🍀']
ITEMS_COLLECTION_EMOJI = ['🍒', '🍉', '🍇', '🍋', '🛡', '💎', '💲', '🔔', '🍊', '❤', '🍌', '7', '🍎', '🍀']

ACTUAL_MONEY_LEFT_EMOJI = "\U0001F4B5"
# 💵
print(ITEMS_COLLECTION)

actual_money = 0
free_shots = 0
multiplier = 1

#actual_money = actual_money + int(input("Inserte créditos" + str(ACTUAL_MONEY_LEFT_EMOJI) + ": "))

print("Créditos actuales: " + str(actual_money) + str(ACTUAL_MONEY_LEFT_EMOJI))

#multiplier = int(input("Set the multiplier between 1, 5, 10, 20, 50, 100 or ALL-IN"))

choose1 = random.choice(ITEMS_COLLECTION)
choose2 = random.choice(ITEMS_COLLECTION)
choose3 = random.choice(ITEMS_COLLECTION)

print(choose1, end=" "); time.sleep(0.5); print(choose2, end=" "); time.sleep(0.5); print(choose3, end=" ")


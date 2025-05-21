coins = ('Platinum', 'Gold', 'Silver')

# Convert to list
coins_list = list(coins)
coins_list[0] = "Bronze"

# Convert back to tuple if needed
coins = tuple(coins_list)

print(coins)

prize = 780_000
first_winner = 0.46 * prize
second_winner = prize * 0.32
thrid_winner = prize - (first_winner + second_winner)

print(f"1. {first_winner}\n2. {second_winner}\n3. {thrid_winner}")
num_par = 0
somas = 0

while num_par < 100:
    num_par += 1
    if (num_par % 2) == 0:
        somas += num_par
print(f"{somas}")
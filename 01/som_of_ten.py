accum = 0
cont = 1

while cont < 10:
    entrada = int(input("Digite 10 números: "))
    accum+= entrada
    cont+= 1
    
print(f"A soma dos números é: {accum}")
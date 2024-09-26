
entrada = int(input("Digite qualquer número entre 10 e 20: "))
accum = 0
idx = 0

while True:
    if entrada >= 10 and entrada <= 20:
        idx += 1
        accum += entrada
        entrada = int(input("Digite qualquer número entre 10 e 20: "))
    else:
        break

print(f"Houveram {idx} laços")
print(f"Valor acumulado {accum}")
print(f"A média aritmética dos valores digitados é: {accum/idx}")




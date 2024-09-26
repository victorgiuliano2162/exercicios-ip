tabu = int(input("Digite o valor da tabuada: "))
ini = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

print(f"Tabuada de {tabu}, inciando em {ini} e terminando em {fim}")
while ini <= fim:
    print(f"{tabu} X {ini} = {tabu * ini}")
    ini +=1
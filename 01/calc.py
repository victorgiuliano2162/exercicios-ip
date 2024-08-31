a = int(input("Selecione a operação:\n1 - Adição\n2 - Subtração\n 3 - Multiplicação\n4 - Divisão"))

while a > 4:
    a = int(input("Selecione a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n 4 - Divisão"))
    
if a == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segunro número: "))
    print(f"A soma entre {num1} e {num2} é: {num1 + num2}")
elif a == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segunro número: "))
    print(f"A soma entre {num1} e {num2} é: {num1 + num2}")
elif a == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segunro número: "))
    print(f"A soma entre {num1} e {num2} é: {num1 + num2}")
elif a == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segunro número: "))
    
    if num1 == 0 | num2 == o:
        print("Impossível dividir por 0 bocó")
    else:
        print(f"A divisão entre {num1} e {num2} é: {num1 + num2}")
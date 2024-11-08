#Aluno: Victor Giuliano de Freitas Silva

'''
leia um inteiro não negativo
imprima se ele é primo
'''

num = int(input("Digite o número para verificar se é primo: "))

def calc_primo(num):
    if num > 0:
        if num == 2 or num== 3 or num == 5 or num == 7:
            print(f"{num} é primo") 
        else:     
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
                print(f"{num} é primo")
            else:
                print(f"{num} não é primo")
    else:
        print("Digite um valor positivo")
            
        
calc_primo(num)
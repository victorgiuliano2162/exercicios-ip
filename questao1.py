#Aluno: Victor Giuliano de Freitas Silva

'''
informar o número de participantes
cada participante recebe um valor de 0 a 5

output:
Quantos participantes?

Númeração do participante 1: 2
Númeração do participante 2: 3
Númeração do participante 3: 4

Total: 7

O vencedor é: 

'''
import random

participantes_val = []


def inf_participantes():
    num_part = int(input("Quantos participantes? "))
    popular_lista_participante(num_part)
    

def popular_lista_participante(num):
    cont = 1
    if num == 1:
        print("Quantidade inválida de participantes. Escolha um valor maior que 1.")
        print("")
    else:
        while cont <= num:
            participantes_val.append(random.randint(0, 5))
            cont+=1
        cont = 1
        for part in participantes_val:
            print(f"Númeração do participante: {cont}: {part}")
            cont+= 1
        
def calc_winner2():
    contador = len(participantes_val)
    accum = sum(participantes_val)
    winner = 1
    while accum != 0:
        accum = accum - 1
        if winner < contador:
            winner+= 1
        if accum == 0:
            print("")
            print(f"O vencedor é o participante {winner}")
            
inf_participantes()
calc_winner2()


'''
[0. 0. 0. 0, 0.]

index out of bonds

'''

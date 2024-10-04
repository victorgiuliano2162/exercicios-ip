#Aluno: Victor Giuliano de Freitas Silva

'''
informar o número de participantes
cada participante recebe um valor de 1 a 5

'''
import random

participantes_val = []


def inf_participantes():
    num_part = int(input("Informe o número de participantes: "))
    popular_lista_participante()
    

def popular_lista_participante(num):
    while num == 1:
        print("Quantidade inválida de participantes. Escolha um valor maior que 1.")
        inf_participantes()
    if num > 1:
        participantes_val.append(random.randint(1, num))

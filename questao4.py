#Aluno: Victor Giuliano de Freitas Silva

'''
Ler um número indeterminado de notas
Valores são válidos de 0 a 10
Parar se o valor informado for negativo


output:
motrar quantidade de notas lidas
exibir as notas na ordem em que foram informadas
soma das notas
média das notas
notas acima da média calculada 
'''

notas = [6,7,8,10,2,3,1,0,2,1]

def qtd_notas():
    num = len(notas)
    print(f"Número de notas lidas {num}")
    
def printar_notas():
    print("Notas informadas:")
    for nota in notas:
        print(nota)

def notas_maiores_media():
    media = sum(notas) / len(notas)
    print(f"A média foi de: {media}")
    for nota in notas:
        if nota > media:
            print(f"Notas acima da média {nota:.1f}")

def printar_soma_notas():
    soma = sum(notas)
    print(f"A soma das notas é: {soma}")
    
def printar_media_notas():
        media = sum(notas) / len(notas)
        print(f"A média das notas foi: {media}")

while True:
    nota = float(input("Digite a nota: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    elif nota < 0:
        qtd_notas()
        printar_notas()
        printar_soma_notas()
        printar_media_notas()
        notas_maiores_media()
        break
        
    else:
        print("Digite uma nota válida")
        

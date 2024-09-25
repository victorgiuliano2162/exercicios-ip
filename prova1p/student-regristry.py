'''
- Adição de alunos (solicitar apenas o nome) 
- Edição de informações de nome do aluno
- Remoção de aluno existente
- Adição de notas em aluno existente (no máximo 4 notas)
- Adição de frequência em aluno existente
- Impressão de relatório de situação dos alunos. No relatório deve ser usado uma função para calcular a situação do aluno. 
- Impressão de relatório de uma situação específica (Filtrar por: Aprovado, Reprovado por Falta ou Reprovado por Nota). Nesse caso o usuário precisa informar qual situação que ele planeja filtrar. 

- O programa deve solicitar a carga horária da disciplina
- o aluno tiver menos que 75% de presença, ele está reprovado por falta

output desejado:
Luiz - nota: 6.2 / frequência: 60 aulas - (Reprovado por nota)
'''

#aluno, notas(4), requencia
alunos:dict = {}  
dicio:dict = {"Carlos": "Kawasaki"}
        
def menu():
    entrada = int(input("Selecione a operação desejada: \n1 -> Adicionar aluno \n2 -> Editar informações do aluno \n3 -> Remover aluno \n4 -> Adicionar notas a aluno \n5 -> Adicionar frequência a aluno \n6 -> Relatório dos alunos aprovados \n7 -> Filtar por Reprovados por falta \n8 -> Filtrar pro reprovados por nota \n9 -> Sair do programa:\n"))
    
    validador: bool = True
    
    while validador:
        if entrada == 1:
            adicionar_aluno()
        elif entrada == 2:
            adicionar_aluno()
        elif entrada == 3:
            adicionar_aluno()
        elif entrada == 4:
            adicionar_aluno()
        elif entrada == 5:
            adicionar_aluno()
        elif entrada == 6:
            adicionar_aluno()
        elif entrada == 7:
            adicionar_aluno()
        elif entrada == 8:
            adicionar_aluno()
        elif entrada == 9:
            validador = False
            print("Até breve")
        
def notas_media(lista):
    total = 0
    for item in lista:
        total += item
    return total

def calc_media(lista):
    media = sum_nota(lista_notas) / (len(lista_notas))
    return media

def adicionar_aluno():
    aluno_nota: list = []
    nota = 0
    cont = 0
    nome = input("Informe o nome do aluno: ")
    aluno_info = []
    while cont < 4:
        nota = float(input("Digite a nota do aluno: "))
        aluno_nota.append(nota)
        cont += 1
    
    media = calc_media(aluno_nota)
    
    frequencia = int(input("Informe a frequência do aluno em aulas: "))
    aluno_info = [media, frequencia]
    
    alunos[nome] = aluno_info
    print(alunos)
    print(dicio)


menu()

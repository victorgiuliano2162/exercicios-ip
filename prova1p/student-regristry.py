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
aluno_info = []

def menu():
    validador = True        
    
    while validador:
        
        entrada = int(input('''
        Selecione a operação desejada:
            1 -> Adicionar aluno
            2 -> Editar informações do aluno
            3 -> Remover aluno
            4 -> Relatório dos alunos aprovados
            5 -> Filtar por Reprovados por falta
            6 -> Filtrar pro reprovados por nota
            7 -> Situação geral
            0 -> Sair do programa
            '''))
        
        if entrada == 1:
            adicionar_aluno()
        elif entrada == 2:
            editar_aluno()
        elif entrada == 3:
            remover_aluno()
        elif entrada == 4:
            gerar_relatorio_aprovados()
        elif entrada == 5:
            reprovados_falta()
        elif entrada == 6:
            reprovados_nota()
        elif entrada == 7:
            situacao_geral()
        elif entrada == 0:
            validador = False
            print("Até breve")
        
def notas_media(lista):
    total = 0
    for item in lista:
        total += item
    return total

def calc_media(lista):
    media = sum_nota(lista) / (len(lista))
    return media

def sum_nota(l: list):
    accum = 0
    for item in l:
        accum += item  
    return accum

def adicionar_aluno():
    aluno_nota: list = []
    nota = 0
    cont = 0
    nome = input("Informe o nome do aluno: ")
    while cont < 4:
        nota = float(input("Digite a nota do aluno: "))
        aluno_nota.append(nota)
        cont += 1
    
    media = calc_media(aluno_nota)
    
    frequencia = int(input("Informe a frequência do aluno em aulas: "))
    carga_hor = int(input("A quantidade de aulas da disciplina: "))
    aluno_info = [aluno_nota, media, frequencia, carga_hor]
    
    
    alunos[nome] = aluno_info
    print("Aluno adicionado")

def editar_aluno():
    print(alunos)
    nome = input("Informe o nome do aluno para poder editar as informações: ")

    if nome in alunos:
        dado = int(input('''Qual informação do aluno você deseja alterar? Digite:
1 -> Alterar nome
2 -> Alterar nota
3 -> Alterar média
4 -> Alterar frequência
            '''))
        if dado == 1:
            alunos[nome] = alunos.pop()
        if dado == 2:
            laco = 1
            while laco == 1:
                qtd_notas = int(input("Qual nota você deseja editar? "))
                while qtd_notas > 4:
                    qtd_notas = int(input("Qual nota você deseja editar? Lembre-se de que os alunos só possuem 4 notas "))
                    
                valor = float(input("Informe o valor da nota: "))
                alunos[nome][0][qtd_notas - 1] = valor
            
                laco = int(input('''Deseja editar mais alguma nota? Digite:
                  1 -> Sim
                  2 -> Não
                  '''))
        if dado == 3:
            valor = int(input("Informe o valor da média: "))
            alunos[nome][0][1] = valor
        if dado == 4:
            valor = int(input("Informe a nova frequência: "))
            alunos[aluno_info][0][2] = valor
    else:
        print("Aluno não encontrado")
        nova_op
    print(alunos)
    
def remover_aluno():
    nome = input("Informe o nome do aluno que deseja remover: ")
    
    if nome not in alunos:
        print("Aluno não encontrado, digite novamente ")
        remover_aluno()
    else:
        removido = alunos.pop(nome)
        print("Aluno removido")
    nova_op()
        
def gerar_relatorio_aprovados():
    for aluno, info in alunos.items():
        #falta adicionar a validação por falta
        if calc_media(info[0]) > 6:
            print(f"o {aluno} foi aprovado")
        else:
            print("Nenhum aluno foi aprovado")
            
    nova_op()

def falta_calc():
    for aluno, info in alunos.items():
        print("todo")

def reprovados_falta():
    for aluno, info in alunos.items():
        print("todo")
    print("falta")
    
def reprovados_nota():
    for aluno, info in alunos.items():
        if calc_media(info[0]) < 7:
            a = info[0][2]
            b = info[0][3]
            print(a)
            print(b)
            print(f"O {aluno} foi reprovado")
    print("nota")
    
def nova_op():
    res = input('''Deseja realizar uma nova operação?
1 -> Sim
2 -> Não
''')
    if res == 1:
        validador = True
        print("nova op true")
    else:
        validador = False
        print("Até breve")
        print("nova op false")

def situacao_geral():
    print("todo")
    
menu()

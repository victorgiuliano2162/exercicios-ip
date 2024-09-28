'''
output desejado:
Luiz - nota: 6.2 / frequência: 60 aulas - (Reprovado por nota)
'''

aluno_info = []
#dicionário populado para testes
alunos: dict = {
    "Carlos": [
        [9.4, 8.2],
        8.8,
        60.0
    ],
    "Jonas": [
        [6.0, 4.2, 3],
        4.4,
        55.0
    ],
    "Ulisses": [
        [8.0, 9.8, 10],
        9.26,
        30.0
    ]
}


def menu():
    while True:
        entrada = int(input('''
Selecione a operação desejada:
    1 -> Adicionar aluno
    2 -> Editar informações do aluno
    3 -> Remover aluno
    4 -> Relatório dos alunos aprovados
    5 -> Filtar por Reprovados por falta
    6 -> Filtrar pro reprovados por nota
    7 -> Relatório geral
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
            print("Até breve")
            break


def notas_media(lista):
    total = 0
    for item in lista:
        total += item
    return total


def calc_media(lista):
    media = sum(lista) / (len(lista))
    return media


def adicionar_aluno():
    nome = input("Informe o nome do aluno: ")
    #aluno_info = [[], 0, 0]
    alunos[nome] = aluno_info
    print("Aluno adicionado")


def editar_aluno():
    nome = input("Informe o nome do aluno para poder editar as informações: ")
    if nome in alunos:
        dado = int(input('''
Qual informação do aluno você deseja alterar? Digite:
    1 -> Alterar nome
    2 -> Adicionar nota
    3 -> Alterar notas do aluno
    4 -> Adicionar média
    5 -> Alterar frequência
'''))
        if dado == 1:
            new_name = input("Informe o novo nome do aluno: ")
            alunos[new_name] = alunos[nome]
            del alunos[nome]
        elif dado == 2:
            aluno_nota = []
            cont = 1
            qtd_notas = int(input("Quantas notas você deseja adiconar? "))
            while cont <= qtd_notas:
                valor = float(input("Informe o valor da nota: "))
                aluno_nota.append(valor)
                cont += 1
            media = calc_media(aluno_nota)
            aluno_info = [aluno_nota, media, 0]
            alunos[nome] = aluno_info
            print(alunos)
        elif dado == 3:
            laco = 1
            while laco == 1:
                qtd_notas = int(input("Qual nota você deseja editar? "))
                valor = float(input("Informe o valor da nota: "))
                alunos[nome][0][qtd_notas - 1] = valor
                laco = int(input('''
Deseja editar mais alguma nota? Digite:
    1 -> Sim
    2 -> Não
'''))
        elif dado == 4:
            valor = int(input("Informe o valor da média: "))
            alunos[nome][0][1] = valor
        elif dado == 5:
            valor = int(input("Informe a nova frequência: "))
            alunos[nome][2] = valor
    else:
        print("Aluno não encontrado")


def remover_aluno():
    nome = input("Informe o nome do aluno que deseja remover: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido")
    else:
        op = int(input('''
Aluno não encontrado
Deseja tentar outra vez?
Digite:
    1 -> Sim
    2 -> Não
'''))
        while op != 2:
            remover_aluno()


def per_cent_presen(valor):
    return (valor/60) * 100


def gerar_relatorio_aprovados():
    for aluno, info in alunos.items():
        pres = per_cent_presen(info[2])
        if calc_media(info[0]) > 6 and pres >= 75:
            print(
                f"{aluno} - nota: {info[1]:.2f} / frequência: {info[2]:.0f} aulas - (Aprovado)")


def reprovados_falta():
    for aluno, info in alunos.items():
        pres = per_cent_presen(info[2])
        if pres < 75:
            print(
                f"{aluno} - nota: {info[1]:.2f} / frequência: {info[2]:.0f} aulas - (Reprovado por falta)")


def reprovados_nota():
    for aluno, info in alunos.items():
        if calc_media(info[0]) < 7:
            print(
                f"{aluno} - nota: {info[1]:.2f} / frequência: {info[2]:.0f} aulas - (Reprovado por nota)")


def situacao_geral():
    for aluno, info in alunos.items():
        pres = per_cent_presen(info[2])
        if calc_media(info[0]) > 6 and pres >= 75:
            print(
                f"{aluno} - nota: {info[1]:.2f} / frequência: {info[2]:.0f} aulas - (Aprovado)")
        elif calc_media(info[0]) < 7 and pres >= 75:
            print(
                f"{aluno} - nota: {info[1]:.2f} / frequência: {info[2]:.0f} aulas - (Reprovado por nota)")
        else:
            print(
                f"{aluno} - nota: {info[1]:.2f} / frequência: {info[2]:.0f} aulas - (Reprovado por falta)")


menu()

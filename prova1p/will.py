

alunos = {}
aluno_info = []
aluno_nota = [5, 5, 5, 5]
media = 5
frequencia = 20

aluno_info = [aluno_nota, media, frequencia]

alunos["Victor"] = aluno_info

print(alunos)

alunos["Victor"][0][0] = 1
hmm = alunos["Victor"][0][0]
print(alunos)
print(hmm)


def lixao():
    aluno_nota: list = []
    nota = 0
    cont = 0
    while cont < 4:
        nota = float(input("Digite a nota do aluno: "))
        aluno_nota.append(nota)
        cont += 1

    media = calc_media(aluno_nota)
    requencia = int(input("Informe a frequência do aluno em aulas: "))
    carga_hor = int(input("A quantidade de aulas da disciplina: "))
    aluno_info = [aluno_nota, media, frequencia, carga_hor]
    aluno[nome] = aluno_info
    '''
    Feito:
    inserir aluno
    editar todas as info do aluno
        
        
    output desejado:
    Luiz - nota: 6.2 / frequência: 60 aulas - (Reprovado por nota) 

    '''
#media alunos[nome][1] = valor
#freq alunos[nome][2] = valor
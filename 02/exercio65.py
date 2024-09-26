dicionario_unid = {1: "um", 2 : "dois", 3: "tres", 4: "quatro", 
                   5: "cinco", 6: "seis",7: "sete",8:"oito", 9: "nove", 0: "zero"}
dicionario_dez = {10: "dez"}
dicionario_cent = {100: "cem"}


for i in range(1,11):
    if i < 10:
        print(i, len(dicionario_unid[i]))
    else:
        print(i, len(dicionario_dez[i]))
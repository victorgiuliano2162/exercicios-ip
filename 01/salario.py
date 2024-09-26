val_hora = float(input("Digite valor da hora do funcionário: "))
num_horas = float(input("Digite a quantidade de horas trabalhadas: "))

sal_bruto = val_hora * num_horas

if sal_bruto <= 900:
    irpf = 0
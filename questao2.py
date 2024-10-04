#Aluno: Victor Giuliano de Freitas Silva


'''
ler número positivo
calcular fib até o primeiro número superior a ele
'''

def fib(num):
    cont = 0
    seq = [0, 1]
    fib_val = 0
    while num > fib_val:
        fib_val = seq[0] + seq[1]
        seq[0] = seq[1]
        seq[1] = fib_val
        print(fib_val)
        cont+= 1
        
fib(100)

#certeza que deve existir uma forma menos burra de resolver isso kkkkkkk
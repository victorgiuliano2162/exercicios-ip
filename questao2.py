#Aluno: Victor Giuliano de Freitas Silva


'''
ler número positivo
calcular fib até o primeiro número superior a ele
'''

def fib(num):
    seq = [0, 1]
    fib_val = 0
    while num > fib_val:
        fib_val = seq[0] + seq[1]
        seq[0] = seq[1]
        seq[1] = fib_val
        print(fib_val)
        
fib(30)

#certeza que deve existir uma forma menos burra de resolver isso kkkkkkk
#essa forma é menos burra do que parece
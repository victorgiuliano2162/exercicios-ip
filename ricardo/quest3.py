'''
input =  um inteiro positivo
imprimir fibbonaci até o primeiro número superior ao número informado

1 2

0 1
 
0 1 1 2 3 5 8 13 21...
'''


entrada = int(input("Digite um número "))

def fib(num):
    if num < 0:
        print("Só aceitamos números positivos")
    
        val1 = 0
        al2 = 1
        val_fib = 0
        while True:
            val1 = val2
            val2 = val_fib
            val_fib = val1 + val2
            print(val_fib)
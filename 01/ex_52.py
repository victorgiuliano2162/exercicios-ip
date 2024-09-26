saque = int(input("Qual valor você deseja sacar? "))
cedulas100;
cedulas50;
cedulas20;
cedulas10;
cedulas5;
cedulas2;
cedulas1;

if saque < 1:
    print("Impossível realizar a operação")
else:
    if saque % 100 == 0:
        cedulas100 = saque/100
        print(f"Serão necessárias {cedulas100:.0f} de 100")
        saque -= cedulas100 * 100

    if saque % 50 == 0:
        cedulas100 = saque/50
        print(f"Serão necessárias {cedulas50:.0f} de 50")
        saque -= cedulas50 * 50
        
    if saque % 20 == 0:
        cedulas100 = saque/20
        print(f"Serão necessárias {cedulas20:.0f} de 50")
        saque -= cedulas50 * 50
        
    if saque % 10 == 0:
        cedulas100 = saque/10
        print(f"Serão necessárias {cedulas10:.0f} de 50")
        saque -= cedulas50 * 50
        
    if saque % 5 == 0:
        cedulas100 = saque/5
        print(f"Serão necessárias {cedulas5:.0f} de 50")
        saque -= cedulas50 * 50
        
        
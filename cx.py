saldo = 1000
a = 0
while a != 4: 
    print("========CAIXA ELETRONICO========\n")
    print("1 - Consultar Saldo \n2 - Realizar Deposito \n3 - Realizar Saque \n4 - Sair")
    a = int(input("Escolha uma dessas opçoes: \n"))
    if a == 1:
        print(f"Seu Saldo Atual É R${saldo}")
    elif a == 2:
        depo = int(input("Quanto voce gostaria de depositar ? \n"))
        if depo < 0:
            print("Deposito nao pode ser realizado pois é negativo\n")
        else:
            saldo = saldo + depo
            print("Deposito realizado com sucesso\n")
    elif a == 3:
        saque = int(input("Quanto voce gostaria de sacar ? \n"))
        if saque <= saldo:
            print("Saque realizado com sucesso\n")
            saldo = saldo - saque 
        elif saque < 0:
            print("Nao é possivel realizar o saque pois o pedido é negativo\n")
        elif saque > saldo:
            print("Nao é possivel realizar o saque pois falta saldo\n")
        else: 
            print("Saque realizado com sucesso")
            saldo = saldo - saque 
    elif a== 4:
        print("Voce saiu do sistema\n") 

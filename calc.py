print("Calculadora")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Escolha a operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    resultado = n1 + n2
    print("O resultado da soma é: ", resultado)
if opcao == 2:
    resultado = n1 - n2
    print("O resultado da subtração é: ", resultado)
if opcao == 3:
    resultado = n1 * n2
    print("O resultado da multiplicação é: ", resultado)
if opcao == 4:
    if n2 != 0:
        resultado = n1 / n2
        print("O resultado da divisão é: ", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")

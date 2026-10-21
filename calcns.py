print("===== RELATORIO DO ALUNO =====\n")
a = 1
soma = 0
menor = 11
maior = -1
ntal = 0
nome = input("Digite o nome do aluno: ")
nn = int(input("Digite a quantidade de notas que utilizara: "))
while( nn >= a):

    nota = int(input("Digite a nota: ")) 
    a = a + 1
    soma = soma + nota
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    if nota >= 7:
        ntal = ntal + 1
media = soma / nn
print(f"\n\n=======================\nAluno : {nome}\nQuantidade de notas: {nn}\nMedia final: {media:.2f}\nMaior nota: {maior}\nMenor nota: {menor}\nNotas 7>=: {ntal} ")
if media >= 6:
    print("Situação: Aprovado")
else: 
    print("Situação: Reprovado")

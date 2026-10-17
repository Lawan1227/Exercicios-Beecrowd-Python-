cod , quanti, valUn = input().split()
cod2 , quanti2, valUn2 = input().split()
total = (int(quanti) * float(valUn)) + (int(quanti2) * float(valUn2))

print(f"VALOR A PAGAR: R$ {total:.2f}")

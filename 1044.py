A , B = input("").split()
B = int(B)
A = int(A)

if A % B == 0 or  B % A ==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

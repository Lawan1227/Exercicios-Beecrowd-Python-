a = 0
while(a == 0):
    n1 = float(input(""))
    if 0 >= n1 or n1 >= 11:
        print("nota invalida")
    else:  
        a = 1
    

while(a == 1):
    n2 = float(input(""))
    if 0 >= n2 or n2 >= 11:
        print("nota invalida")
    else:  
       
        a = 0
    
media = (n1 + n2)/2

print(f"media = {media}")

cod , quant = input("").split()
quant = int(quant)
cod = int(cod)
cach= quant * 4
xsal= 4.5 * quant
xbaco= 5 * quant
torr= 2 * quant
refri= 1.5 * quant



if cod == 1:
    print(f"Total: R$ {cach:.2f}")
elif cod == 2:
    print(f"Total: R$ {xsal:.2f}")
elif cod == 3:
    print(f"Total: R$ {xbaco:.2f}")
elif cod == 4:
    print(f"Total: R$ {torr:.2f}")
elif cod == 5:
    print(f"Total: R$ {refri:.2f}")

idade = int(input())
ano = idade // 365
restdi = idade % 365
mes = restdi // 30
dias = restdi % 30
print(f"{ano:.0f} ano(s)\n{mes:.0f} mes(es)\n{dias} dia(s)")

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

total = sum(faturamento)
print(total)

def percentual(arg):
    percentual_estado = arg * 100
    porcentagem = percentual_estado / total
    
    print(f"A porcentagem é de: {porcentagem}%")


percentual(sp)
percentual(rj)
percentual(mg)
percentual(es)
percentual(outros)
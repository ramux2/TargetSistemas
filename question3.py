import json

with open("dados.json") as file:
    data = json.load(file)

faturamento = []

x = 0
while x <= len(data) - 1:
    y = data[x]["valor"]
    if y == 0.0:
        x += 1
        continue
    faturamento.append(y)
    x += 1

average = sum(faturamento) / len(faturamento)
above_average = 0

for i in faturamento:
    if i > average:
        above_average += 1

print(f"Menor faturamento em um dia do mês: {min(faturamento)}")
print(f"Maior faturamento em um dia do mês: {max(faturamento)}")
print(f"Dias no mês com faturamento diário acima da média: {above_average}")

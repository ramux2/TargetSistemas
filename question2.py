vetor = []
fibonacci = [0, 1]

numb = int(input("Digite um número: "))

t1 = 0
t2 = 1

vetor.append(t2)

print(f"{t1} →  {t2}", end="")

for x in range(numb):
    t3 = t1 + t2
    print(f" →  {t3}", end="")
    vetor.append(t3)
    fibonacci.append(t3)

    t1 = t2
    t2 = t3

print()

if numb in fibonacci:
    indice = fibonacci.index(numb)
    print(f"{numb} encontrado na posição {indice}")

else:
    print("Número não encontrado")
string = input("Digite um texto para inverter: ")

print(string[::-1])

string_invertida = []

i = len(string)
while i > 0:
    string_invertida += string[i-1]

    i = i - 1

print(string_invertida)



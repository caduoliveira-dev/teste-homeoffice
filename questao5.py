string = "exemplo"  # string a ser invertida
invertida = ""  # string vazia para armazenar o resultado

# percorre a string original de trás para frente, adicionando cada caractere na nova string
for i in range(len(string)-1, -1, -1):
    invertida += string[i]

print(invertida)  # imprime a string invertida

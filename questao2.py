# Solicita ao usuário que informe um número
numero = int(input("Informe um número: "))

# Inicia a sequência de Fibonacci com os valores iniciais
fibonacci = [0, 1]

# Adiciona novos valores à sequência de Fibonacci enquanto o último valor for menor ou igual ao número informado
while fibonacci[-1] <= numero:
    novo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(novo_valor)

# Verifica se o número informado pertence à sequência de Fibonacci
if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

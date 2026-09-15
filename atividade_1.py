primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

inicio = 0
fim = len(primos) - 1
tentativas = 0

while inicio <= fim:
    meio = (inicio + fim) // 2
    tentativas += 1

    if primos[meio] < 67:
        inicio = meio + 1
    else:
        fim = meio - 1

print("Quantidade de primos menores que 67:", inicio)

import random

print("Simulador de Dados para RPG\n")

quant_dados = int(input("Quantos dados você deseja simular: "))
lado_dados = int(input("Defina o número de lados para cada dado: "))

i = 0
soma = 0

while (i < quant_dados):
    num_gerado = random.randint(1,lado_dados)
    print(f"Dado: {i +1}: {num_gerado}")
    soma += 1
    soma += num_gerado
    i += 1

print(f"Soma total: {soma}")    





numero_votos = int(input("Informe quantas pessoas vão votar: "))

opcao_voto = []
for i in range(3):
    opcao_voto.append(input(f"Digite o nome da opção de voto {i + 1}: "))

voto_opcao = [0] * 3

for i in range(numero_votos):
    voto = int(input(f"Voto da pessoa: {i + 1} (1 - {len(opcao_voto)}): ")) 
    if voto < 1 or voto > len(opcao_voto):
        print("Voto inválido. Digite um número entre 1 e 3.")
        i -= 1
        continue
    voto_opcao[voto - 1] += 1 

print("Resultado da votação")
for i in range(len(opcao_voto)):
    porcentagem = voto_opcao[i] / numero_votos * 100
    print(f"{opcao_voto[i]}: {voto_opcao[i]} votos ({porcentagem:.2f}%)")
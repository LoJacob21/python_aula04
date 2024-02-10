import random

num_participantes = int(input("Informe quantas pessoas vão participar do sorteio: "))

participantes = []
for i in range (num_participantes):
    participantes.append(input(f"Digite o nome do participante {i + 1}: "))

random.shuffle(participantes)

sorteio = {}
for i in range(num_participantes):
    sorteio[participantes[i]] = participantes[(i + 1) % num_participantes]

print("\nResultado Sorteio\n")
for amigo_secreto, pessoa in sorteio.items():
    print(f"{amigo_secreto} tirou {pessoa}")



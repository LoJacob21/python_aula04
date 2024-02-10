import random

numero_sorteado = random.randint(1,30)

print("Jogo da advinhação")
print("Adivinha um número de 1 a 30")

for tentativa in range(3):
    palpite = int(input("Tentativa {}: Chute um número: ".format(tentativa+1)))

    if palpite == numero_sorteado:
        print("Parebens você acertou o número!!")

    elif palpite < numero_sorteado:
        print("O número sorteado é maior")
    else:
        print("O número sorteado é menor")

print("Você não conseguiu adivinhar o número. O número correto era {}.".format(numero_sorteado))     
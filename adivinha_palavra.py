import random

with open("palavras.txt", "r") as file:
    allText = file.read()
    palavras = list(map(str, allText.split()))
    palavra = random.choice(palavras)
    digitadas = []
    print('#########################################')
    print('      ADIVINHE A PALAVRA SECRETA!')
    print('#########################################')
    print()

    while True:
        letra = input("Digite uma letra: ")
        if len(letra) > 1:
            print("Digite apenas uma letra")
            continue
        digitadas.append(letra)
        if letra in palavra:
            print(f"Correto! A letra '{letra}' existe na palavra secreta!")
        else:
            print(f'A letra "{letra}" não existe na palavra secreta!')
            digitadas.pop()
        
        secreto_temporario = ''
        for letra_secreta in palavra:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'
        
        if secreto_temporario == palavra:
            print(f"Parabéns! A palavra era {secreto_temporario}.")
            break
        else:
            print(f'Palavra secreta está assim: {secreto_temporario}')
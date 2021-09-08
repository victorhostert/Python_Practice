'''
Perguntas e respostas!
'''
print('\n')
print('\t\t BEM VINDO AO JOGO DE PERGUNTAS E RESPOSTAS')
print('\n')
print('#####################################################')
print(
    "Para responder, digite a letra que está entre colchetes na sua resposta!"
    )
print('\n')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual destes é um réptil?',
        'respostas': {
            'a' : 'Salamandra',
            'b' : 'Tartaruga',
            'c' : 'Sapo',
            'd' : 'Cobra-cega',
        },
        'resposta certa' : 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual destes produtos não pode ser misturado com amônia, correndo o risco de produzir gás mostarda, tóxico para humanos?',
        'respostas': {
            'a' : 'Bicarbonato de sódio',
            'b' : 'Soda cáustica',
            'c' : 'Vinagre',
            'd' : 'Alvejante',
        },
        'resposta certa' : 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Quais são os sobrenomes dos 3 personagens principais no anime Naruto?',
        'respostas': {
            'a' : 'Uzumaki, Haruno e Uchiha',
            'b' : 'Sarutobi, Uchiha e Hyuuga',
            'c' : 'Haruno, Sharingan e Kyuubi',
            'd' : 'Naruto, Sakura e Sasuke',
        },
        'resposta certa' : 'a',
    },
}


respostas_certas = 0
for pergunta_key, pergunta_value in perguntas.items():
    print(f"{pergunta_key}: {pergunta_value['pergunta']}")
    print('Respostas:')
    for rk, rv in pergunta_value['respostas'].items():
        print(f"[{rk}]: {rv}")
   
    resposta_user = input('Sua resposta: ')
   
    if resposta_user == pergunta_value['resposta certa']:
        respostas_certas += 1
        print('Acertaste! Mereces meus parabéns!')
    else:
        print('Erraste irmão, foste bobinho e caiste em minhas perguntas sapecas')
    print()

print(f"Você acertou {respostas_certas} de um total de {len(perguntas)} perguntas")
if respostas_certas < len(perguntas):
    print('Como você não acertou todas, ainda tem o que melhorar! Estude mais! (e veja Naruto)')
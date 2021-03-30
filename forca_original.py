import random


with open('palavras_forca_original.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

palavra = random.choice(lista_de_palavras).upper()

#menu
while True:
    print('_'*20)
    print('MENU')
    print('_'*20)
    print('G-Gravar novas palavras')
    print('J-Jogar')
    print('S-Sair')
    opcao = str(input('Escolha uma opção: '))

#opção de gravar palavras
    if opcao.upper() == 'G':
        print('Digite novas palavras: ')
        add_palavras = ''
        while add_palavras.upper() != 'sair':
            add_palavras = str(input('Qual a palavra? '))
            palavra.apend(add_palavras)
            if add_palavras.upper() == 'sair':
                break

#opção de jogar
    if opcao.upper() == 'J':
        print('--------Bem vindo ao jogo da forca!!---------')
        palavra = random.choice(lista_de_palavras).upper()
        print('Palavra escolhida com sucesso!!')
        print('Voce tem 6 chances para acertar!')
        print('A palavra tem {} letras'.format(len(palavra)))


#desenho da forca. OBS: pode não ter ficado tão bom o desenho haha.
        forca = """ 
        __________
                 |
                 |"""
        vazio = """
        
        
        """
        cabeca ="""
                 O
        """
        tronco = """
                 O
                 |
        """
        braco_esquerdo = """
                 O
                /|
        """
        braco_direito = """
                 O
                /|\\
        """
        perna_esquerda = """
                 O
                /|\\
                /
        """
        perna_direita = """
                 O
                /|\\
                / \\
        """
        #lista do desenho da forca
        chances_do_boneco = [vazio, cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]

        print(chances_do_boneco)

        #variaveis
        acertos = 0
        erros = 0
        letras_acertadas = ''
        letras_erradas = ''
        letras_escolhidas = []

        #loops
        while acertos != len(palavra) and erros != 7:
            mensagem = ''
            for letra in palavra:
                if letra in letras_acertadas:
                    mensagem += f'{letra} '
                else:
                    mensagem += '_ '
            print(forca + chances_do_boneco[erros])
            print(mensagem)

            letra = input('Qual letra: ').upper()
            letras_escolhidas.append(letra)
            print('Letras escolhidas: {}'.format(letras_escolhidas))
            if letra in palavra:
                print('Voce acertou a letra!')
                letras_acertadas += letra
                acertos += palavra.count(letra)

            else:
                print('Voce errou')
                letras_erradas += letra
                erros += 1

            if erros >= 6:
                print('Voce perdeu!! Tente outra vez.')




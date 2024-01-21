def adivinhacao():

    print("*"*32)
    print("Bem vindo ao jogo de advinhação!")
    print("*"*32)
    from typing import Final
    # Python, sendo uma linguagem dinâmica, não tem o recurso de "constantes". Para o pyton tudo e objeto. Esse módulo cria uma Pseudo constante
    import random

    numero_secreto = random.randrange(1, 101)
    totaldetentativas = 5
    tentativa: Final = totaldetentativas
    rodada = 1


    while (totaldetentativas > 0):
        print('Tentativa {} de {}'.format(rodada, tentativa))
        chute = int(input("Digite um numero entre 1 e 100:  "))
        print("Voce digitou:{} ".format(chute))
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto



        if (chute < 1 or chute > 100):
            print('!'*20+' ATENCAO '+'!'*20)
            print("Voce deve digitar APENAS um numero ENTRE 1 e 100!!")
            print("=" * 50)
            continue

        if (acertou):
            print("="*30)
            print(f'Parabens voce acertou!!!!! Venda o terreno e jogue no Tigrinho. O Numero Secreto era {numero_secreto}')
            print("=" * 30)
            newgame = input('Deseja jogar novamente? (S/N)')
            ng = newgame.upper()
            ngs = ng == 'S'
            ngn = ng == 'N'

            if ngs:
                print("=" * 30)
                print('Ola de novo !!')
                print("=" * 30)
                numero_secreto = int(random.randrange(1, 101))
                totaldetentativas = tentativa
                rodada = 0

            else:
                if ngn:
                    break

        else:
            if (maior):
                print("="*30)
                print("Voce errou! o seu chute foi maior que o numero secreto.")
                print("="*30)
            elif (menor):
                print("="*30)
                print("Voce errou! o seu chute foi menor que o numero secreto.")
                print("="*30)
        totaldetentativas = totaldetentativas-1
        rodada = rodada + 1

        if totaldetentativas == 0:
            print("=" * 30)
            c = input('Deseja tentar de novo? (S/N): ')
            letra = c.upper()
            s = letra == 'S'
            n = letra == 'N'

            if s:
                trocanum = input('Deseja manter (M) ou trocar(T) o numero secreto?(M/T)')
                tn = trocanum.upper()
                m = tn == 'M'
                t = tn == 'T'

                if t:
                    print('!' * 10 + ' ATENÇÃO ' + '!' * 10)
                    print('O Numero Secreto mudou!')
                    print("=" * 30)
                    numero_secreto = int(random.randrange(1, 101))
                    print(numero_secreto)
                    totaldetentativas = tentativa
                    rodada = 1
                    continue
                else:
                    if m:
                        totaldetentativas = tentativa
                        rodada = 1
                        continue

            else:
                if n:
                    print("=" * 30)
                    print(f'O numero secreto era {numero_secreto} . Boa sorte na proxima!')
                    break



    print("=" * 30)
    print(f'Fim de jogo. Obrigado pela sua presença!!')

if __name__ == '__main__':
    adivinhacao()

from time import sleep

c = ('\033[m',           #0 - sem cor
     '\033[0:30:41m',    #1 - vermelho
     '\033[0:30:42m',    #2 - verde
     '\033[0:30:43m',    #3 - amarelo
     '\033[0:30:44m',    #4 - azul
     '\033[0:30:45m',    #5 - roxo
     '\033[7:40m',       #6 - branco
     '\033[4:31:47m',    #7 - underline,vermelho,fundo cinza
      );


def titulo(msg, cor=0):
    print(c[cor], end='')
    print(f'{"":_^93}')
    print(f'{msg:.^93}')
    print(f'{"":_<93}')
    print(c[0], end='')


def frase(msg, cor=0):

    print(c[cor], end='')
    print(f'{msg}', end='')
    espera(' | ',f'{" |  |  |  |  |  Escolha as seguintes opções:":.<73}\n'
'[1]-Dados Pessoas | [2]-Experiências Profissionais | [3]-Objetivos | [4]-Formações | [5]-Sair')
    print(c[0], end='')


def espera(msg='', msg2='', cor=6):
    print(c[cor], end='')
    tempo = 0
    while tempo < 3:
        print(f'{msg}', end='')
        sleep(0.5)
        tempo += 1
    print(msg2)
    print(c[0], end='')


def validaint(msg='> ', cor=0):
    while True:
        print(c[cor], end='')
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[4:31:47m', end='')
            print(f'{"ERRO, INFORME APENAS NÚMEROS POR FAVOR":^94}')
            print('\033[m', end='')
            frase('Reiniciando', 6)
            continue
        except (KeyboardInterrupt):
            print('\033[4:31:47m', end='')
            print('Usuário interropeu o programa.')
            print('\033[m', end='')
            return 0
        else:
            print(c[cor], end='')
            return n

            
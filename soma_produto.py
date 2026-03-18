from time import sleep
num_s = []
num_m = []
def soma():
    print()
    print('      ==================')
    print('\033[1;34mSOMA\033[m'.center(40))
    print('      ==================')
    print()
    while True:
        try:
            print()
            print('——'*15)
            print()
            n1 = float(input('Digite o 1° número: '))
            n2 = float(input('Digite o 2° número: '))
            soma = n1 + n2
            num_s.append(soma)
            print()
            if soma.is_integer():
                print(f'O resultado é: {int(soma)}')
                print()
                print('-='*15)
            else:
                print(f'O resultado é: {soma}')
                print()
                print('-='*15)

            while True:
                choice = input('Deseja somar de novo? (S/N): ').strip().upper()
                if choice.startswith('S'):
                    break

                elif choice.startswith('N'):
                    print()
                    sleep(0.2)
                    print('Voltando para o \033[1;34mMENU\033[m')
                    for i in range (3, 0, -1):
                        i = '*'
                        print(i)
                        sleep(0.5)
                    return

                else:
                    print('Digite apenas \033[1;34mS ou \033[1;31mN\033[m!')
        except ValueError:
            print()
            print('\033[1;91mERRO\033[m. Digite apenas números.')

def mult():
    while True:
        print()
        print('      ==================')
        print('\033[1;35mMULTIPLICAÇÃO\033[m'.center(40))
        print('      ==================')
        print()
        try:
            m1 = float(input('Digite o 1° número: '))
            m2 = float(input('Digite o 2° número: '))
            multi = m1 * m2
            num_m.append(multi)
            print()
            if multi.is_integer():
                print(f'O resultado é: {int(multi)}')
                print()
                print('-='*15)
            else:
                print(f'O resultado é {multi:.2f}')
                print()
                print('-='*15)
            while True:
                choice = input('Deseja multiplicar de novo?(S/N): ').strip().upper()
                if choice.startswith('S'):
                    break
                elif choice.startswith('N'):
                    print()
                    sleep(0.2)
                    print('Voltando para o \033[1;34mMENU\033[m')
                    for i in range (3, 0, -1):
                        i = '*'
                        print(i)
                        sleep(0.5)
                    return
                else:
                    print('Digite apenas \033[1;34mS ou \033[1;31mN\033[m!')
        except ValueError:
            print()
            print('\033[1;91mERRO\033[m. Digite apenas números.')

def maior():
    while True:
        if not num_s and not num_m:
            print()
            sleep(0.2)
            print('\033[1;31mNÃO HÁ\033[m números no momento')
            print()
            sleep(0.4)
            print('Voltando ao \033[1;34mMENU\033[m')
            for c in range (3, 0, -1):
                c = '*'
                print(c)
                sleep(0.5)
            break
        else:
            if num_s and not num_m:
                print()
                print('MAIOR NÚMERO'.center(40))
                print('          ————————————————————')
                print(f'SOMA: {max(num_s)}'.center(40))
                print('Não há produtos.'.center(40))
                print(f'LISTA: {num_s}'.center(40))
                print()
            elif num_m and not num_s:
                print()
                print('MAIOR NÚMERO'.center(40))
                print('          ————————————————————')
                print('Não há somas'.center(40))
                print(f'PRODUTO: {max(num_m)}'.center(40))
                print(f'LISTA: {num_m}'.center(40))
                print()
            else:
                print()
                print('MAIOR NÚMERO'.center(40))
                print('          ————————————————————')
                print(f'SOMA: {max(num_s)}'.center(40))
                print(f'PRODUTO: {max(num_m)}'.center(40))
                print()
                print(f'LISTA SOMA: {num_s} | LISTA MULTIPLICAÇÃO: {num_m}')
                print()
            while True:
                choice = input('Quer voltar ao menu? (S/N): ').strip().upper()
                if choice.startswith('S'):
                    sleep(0.2)
                    print('Voltando para o \033[1;34mMENU\033[m')
                    for c in range (3, 0, -1):
                        c = '*'
                        print(c)
                        sleep(0.5)
                    return
                elif choice.startswith('N'):
                    print()
                    print('ok')
                    break
                else:
                    print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m')

def novos():
    while True:
                                             #HERE, THIS CODE LINE HAPPENS IF WE HAVE ONLY SUMS / AQUI, ESTA LINHA DE CÓDIGO OCORRE SE TIVERMOS SÓ SOMAS
        if not num_s and not num_m:
            print()
            sleep(0.2)
            print('\033[1;31mNÃO HÁ\033[m números no momento.')
            print()
            sleep(0.2)
            print('Voltando ao \033[1;34mMENU\033[m')
            for m in range (3, 0, -1):
                m = '*'
                print(m)
                sleep(0.5)
            break
        print()
        choice = input('Deseja acessar este menu?: ').strip().upper()

        if choice.startswith('S'):
                print()
                print('      ==================')
                print('\033[1;34mMAIORES\033[m'.center(40))
                print('      ==================')
                print()

                if num_s and not num_m:
                    print(f'Maior soma: {max(num_s)}')
                    print()
                    change = input('Deseja alterar esse valor? (S/N): ').strip().upper()
                    print()

                    if change.startswith('S'):
                        print()

                        while True:
                            troca_s1 = input('Novo N1: ')
                            troca_s2 = input('Novo N2: ')

                            n_soma = float(troca_s1) + float (troca_s2)
                            indice = num_s.index(max(num_s))

                            num_s.pop(indice)
                            num_s.append(n_soma)
                            print(f'Nova lista: {num_s}')
                            print()
                            again = input('Deseja alterar novamente? (S/N): ').strip().upper()
                            print()

                            if again.startswith('S'):
                                continue

                            elif again.startswith('N'):
                                print('Voltando ao \033[1;34mMENU\033[m')
                                sleep(0.2)
                                for c in range(3, 0, -1):
                                    c = '*'
                                    print(c)
                                    sleep(0.5)
                                return

                            else:
                                print()
                                print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m.')

                    elif change.startswith('N'):
                        sleep(0.2)
                        print('Voltando ao \033[1;34mMENU\033[m')
                        for c in range(3, 0, -1):
                            c = '*'
                            print(c)
                            sleep(0.5)
                        break

                    else:
                        print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m')

                                             #HERE, THIS CODELINE HAPPENS IF WE HAVE ONLY MULTIPLICATIONS / AQUI, ESTA LINHA DE CÓDIGO OCORRE SE TIVERMOS SÓ MULTIPLICAÇÕES
                elif num_m and not num_s:
                    print(f'Maior multiplicação: {max(num_m)}')
                    print()
                    change_m = input('Deseja alterar esse valor? (S/N): ').strip().upper()
                    print()

                    if change_m.startswith('S'):
                        print()

                        while True:
                            troca_m1 = input('Novo N1: ')
                            troca_m2 = input('Novo N2: ')

                            n_mult = float(troca_m1) * float(troca_m2)
                            indice_m = num_m.index(max(num_m))

                            num_m.pop(indice_m)
                            num_m.append(n_mult)
                            print(f'Nova lista: {num_m}')
                            print()
                            again = input('Deseja alterar novamente? (S/N): ').strip().upper()
                            print()

                            if again.startswith('S'):
                                continue

                            elif again.startswith('N'):
                                print('Voltando ao \033[1;34mMENU\033[m')
                                sleep(0.2)
                                for c in range (3, 0 , -1):
                                    c = '*'
                                    print(c)
                                    sleep(0.5)
                                return

                            else:
                                print()
                                print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m.')

                                   #HERE, THIS CODELINE HAPPENS IF WE HAVE BOTH SUMS AND MULTIPLICATIONS / AQUI, ESTA LINHA DE CÓDIGO OCORRE SE TIVERMOS TANTO SOMAS QUANTO MULTIPLICAÇÕES.
                elif num_s and num_m:
                    print(f'Maior soma: {max(num_s)} | Maior Multiplicação: {max(num_m)}')
                    print()
                    print(f'\033[1;34mLISTA SOMA\033[m: {num_s} | \033[1;35mLISTA MULTIPLICAÇÃO\033[m: {num_m}')
                    print()
                    change = input('Deseja alterar esses valores? (S/N): ').strip().upper()

                    if change.startswith('S'):
                        print()

                        while True:
                            print('Qual valor deseja trocar?')
                            print(f'\033[1;34mSOMA\033[m: {max(num_s)} | \033[1;35mMULTIPLICAÇÃO\033[m : {max(num_m)}')
                            print()
                            wich = input('> ').strip().upper()

                            if wich.startswith('S'):

                                while True:
                                    troca_s1 = input('Novo N1: ')
                                    troca_s2 = input('Novo N2: ')

                                    n_soma = float(troca_s1) + float(troca_s2)
                                    indice = num_s.index(max(num_s))

                                    num_s.pop(indice)
                                    num_s.append(n_soma)
                                    print(f'Nova lista: {num_s}')
                                    again = input('Deseja alterar novamente? (S/N): ').strip().upper()
                                    print()
                                    if again.startswith('S'):
                                        continue

                                    elif again.startswith('N'):
                                        sleep(0.2)
                                        print('Voltando ao \033[1;34mMENU\033[m')
                                        sleep(0.2)
                                        for c in range (3, 0, -1):
                                            c = '*'
                                            print(c)
                                            sleep(0.5)
                                        return

                                    else:
                                        print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m.')

                            elif wich.startswith('M'):

                                while True:
                                    troca_m1 = input('Novo N1: ')
                                    troca_m2 = input('Novo N2: ')

                                    n_mult = float(troca_m1) * float(troca_m2)
                                    indice = num_m.index(max(num_m))

                                    num_m.pop(indice)
                                    num_m.append(n_mult)
                                    print(f'Nova lista: {num_m}')
                                    again = input('Deseja alterar novamente?(S/N): ').strip().upper()
                                    if again.startswith('S'):
                                        continue

                                    elif again.startswith('N'):
                                        sleep(0.2)
                                        print('Voltando ao \033[1;34mMENU\033[m')
                                        sleep(0.2)
                                        for c in range (3, 0 , -1):
                                            c = '*'
                                            print(c)
                                            sleep(0.5)
                                        return

                                    else:
                                        print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m.')

                    elif change.startswith('N'):
                        sleep(0.2)
                        print('Voltando ao \033[1;31mMENU\033[m')
                        sleep(0.2)
                        for c in range (3, 0, -1):
                            c = '*'
                            print(c)
                            sleep(0.5)
                        return

                    else:
                        print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m ')



        elif choice.startswith('N'):
            print()
            print('Voltando ao \033[1;34mMENU\033[m')
            sleep(0.2)
            for c in range (3, 0, -1):
                c = '*'
                print(c)
                sleep(0.5)
            return

        else:
            print('Digite apenas \033[1;34mS\033[m ou \033[1;31mN\033[m')

while True:
    print('-='*15)
    print('\033[1;35mCalculadora\033[m'.center(40))
    print('-='*15)
    print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair')
    print()
    menu = input('> ').strip().upper()
    if menu == '1' or menu.startswith('SOM'):
        soma()

    elif menu == '2' or menu.startswith('MULTI'):
        mult()

    elif menu == '3' or menu.startswith('MAI'):
        maior()

    elif menu == '4' or menu.startswith('NOV'):
        novos()

    elif menu == '5' or menu.startswith('SA'):
        print()
        sleep(0.2)
        print('Finalizando...')
        sleep(0.2)
        for c in range (3, 0, -1):
            c = '*'
            print(c)
            sleep(0.5)
        sleep(1)
        exit()
from time import sleep

while True:
    print('=' * 30)
    print('{:^30}'.format('BANCO DEV'))
    print('=' * 30)
    valor = int(input('Qual valor você quer sacar? '))
    total = valor
    ced = 100
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} de R${ced}!')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            totced = 0
            if total == 0:
                print('Finalizando...!')
                sleep(2)
                print('Volte sempre!')
                break

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('Solicitação encerrada!')
        break
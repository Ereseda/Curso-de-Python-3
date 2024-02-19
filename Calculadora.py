while True:
    N_1 = input('Digite um número: ')
    N_2 = input('Digite outro número: ')
    OP = input('Digite o operador (+ - / *): ')

    N_Validos = None

    try:
        N_1_Float = float(N_1)
        N_2_Float = float(N_2)
        N_Validos = True
    except:
        N_Validos = None
    if N_Validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    Op_Permitidos = '+ - / *'  

    if OP not in Op_Permitidos:
        print('Operador Inválido.')
        continue
    if len(OP) > 1:
        print('Digite apenas um operador.')
        continue

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair is True:
        break
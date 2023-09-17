lista_colaboradores = []
id_global = 0
dic = {}
# --------------- CADASTRO DE COLABORADOR ---------------
def cadastrar_colaborador(id_global):
    # Optei por não adicionar o ID dentro do dic e isso acabou sendo uma má escolha.
    dic['Nome'] = input('Nome do Colaborador: ')
    dic['Setor'] = input('Setor: ')
    dic['Salário'] = float(input('Pagamento R$'))
    lista_colaboradores.append(dic.copy())

# --------------- CONSULTA DE COLABORADOR ---------------
def consultar_colaborador():
    op = 5
    while op != 1 and op != 2 and op != 3 and op != 4:
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao Menu')
        op = int(input('>> '))
        print('--' * 20)
        if op > 4 or op < 1:
            print('\033[:31mOPÇÃO INVÁLIDA!\033[m')
        if op == 1:
            nid = 0
            for c in lista_colaboradores:
                nid += 1
                print(f'ID: {nid}')   # Os colaboradores não terão ID fixo por conta da minha escolha supramencionada.
                for i, a in c.items():
                    print(f'{i}: {a}')
            print('--' * 20)
            op = 5
        elif op == 2:
            nid = int(input('Digite o Id do Colaborador: '))
            print(f'ID: {nid}')  # Se for removido um colaborador e houver mais um a sua frente, este terá o ID do colaborador removido.
            for c, i in lista_colaboradores[nid-1].items():
                print(f'{c}: {i}')
            print('--' * 20)
            op = 5

        elif op == 3:
            setor = input('Digite o setor do(s) Colaborador(es): ')
            for c in lista_colaboradores:
                if c["Setor"] == setor:
                    for i, a in c.items():
                        print(f'{i}: {a}')  # Por conta da minha má escolha, não pude deixar os colaboradores com seus respectivos IDs.
            op = 5
            print('--' * 20)
        else:
            break

# --------------- REMOÇÃO DE COLABORADOR ---------------
def remover_colaborador():
    remov = int(input('Digite o Id do Colaborador que deseja remover: '))
    lista_colaboradores.pop(remov-1)
    print('Colaborador REMOVIDO.')

# --------------- ESCOLHA DE TÍTULOS ---------------
def titulo(txt):
    print('*'*90)
    print('{:-^90}'.format(txt))

# --------------- MENU PRINCIPAL ---------------
print('\033[:94mBem-vindo \033[mao \033[:93mControle de Colaboradores \033[mdo \033[:92mMatheus Henrique Lima de Souza\033[m')
opc = 0
while opc != '4':
    titulo('MENU PRINCIPAL')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Colaborador')
    print('2 - Consultar Colaborador(es)')
    print('3 - Remover Colaborador')
    print('4 - Sair')
    opc = input('>> ')
    if opc == '1':
        titulo('CADASTRAR COLABORADOR')
        cadastrar_colaborador(id_global)
    elif opc == '2':
        titulo('COLABORADORES')
        consultar_colaborador()
    elif opc == '3':
        titulo('REMOÇÃO DE COLABORADOR')
        remover_colaborador()
    else:
        if opc != '4':
            print('\033[:31mOPÇÃO INVÁLIDA\033[m')

# Dedico meus esforços a minha familia, o meu combustível e razão de
# continuar sacrificando todos os meus dias livres para um dia lhes dar uma vida melhor.
print('\033[:32mBem-Vindo \033[ma \033[:93mSorveteria \033[mdo \033[:94mMatheus Henrique Lima de Souza\033[m')
print('{:=^91}'.format('Cardápio'))
print('|  Nº de Bolas  |  Sabor Tradicional (tr)  |  Sabor Premium (pr)  |  Sabor Especial (es)  |')
print('|        1      |          R$6,00          |        R$7,00        |         R$8,00        |')
print('|        2      |          R$11,00         |        R$13,00       |         R$15,00       |')
print('|        3      |          R$15,00         |        R$18,00       |         R$21,00       |')
print('-'*91)
tot = preco = 0 #tot é a variavel que receberá o valor total dos pedidos e preco o valor individual dos mesmos
while True:
    s = input('Digite o sabor de sua escolha [tr/pr/es]: ').lower() # 's' é a variavel que receberá os sabores.
    if s != 'tr' and s != 'pr' and s != 'es':
        print('Sabor inválido. Tente novamente...')
        print('\033[:31mxxx\033[:m'*15)
        continue
    if 'tr' in s:
        esc = 'TRADICIONAL' # 'esc' guardará a string do sabor escolhido.
    elif 'pr' in s:
        esc = 'Premium'
    elif 'es' in s:
        esc = 'Especial'
    b = input('Digite o número de bolas desejado [1/2/3]: ') # 'b' é o número de bolas de sorvete escolhidas.
    if b != '1' and b != '2' and b != '3': # Nota: Decidi dixar o número de bolas de sorvete como string.
        print('Número de bolas inválido. Tende novamente...')
        print('\033[:31mxxx\033[:m'*15)
        continue
    print('...'*15)
    if b == '1' and s == 'tr':
        tot += 6
        preco = 6
    elif b == '2' and s == 'tr':
        tot += 11
        preco = 11
    elif b == '3' and s == 'tr':
        tot += 15
        preco = 15
    elif b == '1' and s == 'pr':
        tot += 7
        preco = 7
    elif b == '2' and s == 'pr':
        tot += 13
        preco = 13
    elif b == '3' and s == 'pr':
        tot += 18
        preco = 18
    elif b == '1' and s == 'es':
        tot += 8
        preco = 8
    elif b == '2' and s == 'es':
        tot += 15
        preco = 15
    elif b == '3' and s == 'es':
        tot += 21
        preco = 21
    print(f'Você pediu {b} bola(s) de sorvete no Sabor {esc}')
    print(f'Valor do pedido: R${preco:.2f}')
    sn = input('Deseja mais algum sorvete? [S/N]: ').upper() # 'sn' receberá o SIM ou o NÃO.
    s = ' ' # Decidi deixar que qualquer outra letra além de 'n' desse fim a execução. Sei que não é o ideal.
    if sn == 'S':
        print('.' * 50)
    else:
        break
print('\033[:94m...\033[m'*15)
print('Valor total do(s) pedido(s): R${:.2f}'.format(tot))

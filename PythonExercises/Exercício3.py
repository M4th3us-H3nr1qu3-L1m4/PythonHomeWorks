valores = []
def cachorro_peso():
    while True:
        # Enquanto o usuário digitar valores númericos o programa vai funcionar em baixo do try.
        try:
            base = 0
            peso = float(input('Qual é o peso do pet? '))
            if peso >= 3 and peso < 10:
                base += 50
                valores.append(base)
                print('')
                break
            elif peso >= 10 and peso < 30:
                base += 60
                valores.append(base)
                print('')
                break
            elif peso >= 30 and peso < 50:
                base += 70
                valores.append(base)
                print('')
                break
            else:
                if peso >= 50:
                    print('Não aceitamos monstros aqui.')
                    print('Esse realmente é o peso de um cachorro?')
                    print('')
                if peso < 3:
                    print('Esse não é o peso de um cachorro, meu consagrado!')
                    print('Por favor entre com o peso do cachorro.')
                    print('')
        # Se ele digitar um valor não númerico o programa falhará, indo então para o expcept.
        except:
            print('Você digitou um valor não númerico')
            print('')
        # Chegando aqui o programa local se repetirá

def cachorro_pelo():
    while True:
        # Se umas das 4 opções forem digitadas o programa entrará no break.
        print('Qual é o pelo do cachorro')
        print('C - pelo curto')
        print('M - pelo médio')
        print('L - pelo longo')
        pelo = str(input('>> ')).upper()                          # Não importa o tamanho que seja digitado sempre
        if pelo != 'C' and pelo != 'M' and pelo != 'L':           # entrará o MAIÚSCULO.
            print('Digite uma das três opções, por favor.')       # Se for digitado qualquer coisa fora das opções
            print('')                                             # o programa voltará a repetir a pergunta até
        elif pelo == 'C':                                         # a opção válida ser digitada.
            mult = 1
            valores.append(mult)
            break
        elif pelo == 'M':
            mult = 1.5
            valores.append(mult)
            break
        elif pelo == 'L':
            mult = 2
            valores.append(mult)
            break

def cachorro_extra():
    extra = 0
    while True:
        print('Deseja adicionar mais algum serviço?')
        print('1 - Corte de Unhas - R$10,00')
        print('2 - Escovar dentes - R$12,00')
        print('3 - Limpeza de Orelhas - R$15,00')
        print('0 - Não desejo adicionais')
        add = str(input('>> '))
        if add == '1':                         # O programa pedirá um adicional até o usuário não desejar mais nada.
            extra += 10                        # Se for digitado qualquer coisa fora de opção o programa voltará
        elif add == '2':                       # a perguntar por um adicional até uma opção válida ser digitada.
            extra += 12
        elif add == '3':
            extra += 15
        elif add == '0':
            valores.append(extra)
            break
        else:
            print('Por favor, digite apenas uma das 4 opçôes')

# Programa Principal
print('\033[:31mBem-Vindo\033[m ao \033[:94mPetshop\033[m do \033[:93mMatheus Henrique Lima de Souza\033[m')
cachorro_peso()
cachorro_pelo()
cachorro_extra()
total = valores[0] * valores[1] + valores[2]
print(f'Total a pagar R${total:.2f} (Peso: {valores[0]} x Pelo: {valores[1]} + adicional(ais): {valores[2]})')
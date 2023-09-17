print('\033[:34mSeja Bem-Vindo \033[ma loja do \033[:93mMatheus Henrique Lima de Souza \033[m;)') #Apresentação
v = float(input('\033[:36mQual o valor do Produto? \033[:32mR$'))
q = int(input('\033[:36mQual é a quantidade do produto? \033[m'))
val = v*q #Calculo do valor total dos produtos
print('\033[:96mValor Total do Produto: \033[:92mR${:.2f}'.format(val))
if 200 <= q < 1000:
    des = val - (5/100*val) #Subtração do produto por 5% do valor do mesmo
    print('\033[:96mValor com desconto aplicado: \033[mR${:.2f}'.format(des))
elif 1000 <= q < 2000:
    des = val - (10/100*val) #Subtração do produto por 10% do valor dele
    print('\033[:96mValor com desconto aplicado: \033[mR${:.2f}'.format(des))
elif q >= 2000:
    des = val - (15/100*val) #Subtração do produto pr 15% de seu valor
    print('\033[:96mValor com desconto aplicado: \033[mR${:.2f}'.format(des))
else:
    print('\033[:31mNão há aplicação de desconto.')

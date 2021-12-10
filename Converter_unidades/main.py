import model
opcao = 1
print()
print('Bem vindo ao programa.')
print('leia antes as instruções antes de começar! ')
while opcao != '3':
    print()
    print('Escolha uma opção abaixo: ')
    opcao = input('[1] Conversão - [2] Instruções - [3] Encerrar o Programa  : ')
    if opcao == '1':
        model.conversão()

    elif opcao == '2':
        model.instruções()
        
    elif opcao == '3':
        print('saindo do programa')

    else:
        print()
        print('Opção Invalida, leia atentamente e coloque a opção correta! ')
        print()

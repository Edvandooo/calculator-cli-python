

def soma(num1, num2):
    print(num1 + num2)

def subtração(num1, num2):
    print(num1 - num2)

def multiplicação(num1, num2):
    print(num1 * num2)

def divisão(num1, num2):
    if num2 == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        print(num1 / num2)

while True:
    num1 = float(input('Digite o primeiro número: '))

    print(
        'Escolha uma opção abaixo:\n'
        '1 - Opção (1): soma \n'
        '2 - Opção (2): subtração \n'
        '3 - Opção (3): multiplicação \n'
        '4 - Opção (4): divisão \n'
    )
    Menu_choice = input('Digite sua escolha, Ex: 1, 2, 3, 4:  ')

    num2 = float(input('Digite o segundo número: '))


    if Menu_choice == '1':
        soma(num1, num2)
    elif Menu_choice == '2':
        subtração(num1, num2)
    elif Menu_choice == '3':
        multiplicação(num1, num2)
    elif Menu_choice == '4':
        divisão(num1, num2)
    menu_exit = input('Você deseja sair? (S/n?): ')
    if menu_exit.lower() == 's':
        break
    elif menu_exit.lower() == 'n':
        continue
    else:
            print('Argumento inválido, tente novamente. (S/n)')
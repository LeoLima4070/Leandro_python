while True:
    print("=" * 100)
    print("Calculadora".center(100))
    print("=" * 100)
    print("Menu")
    print("+")
    print("-")
    print("x")
    print("/")
    print("0 - Sair")

    operacao = input("Digite a operação que deseja realizar: ")
    
    if operacao == '+':
        numero1 = int(input("Digite um número inteiro: "))
        numero2 = int(input("Digite um número inteiro: "))
        resultado = numero1 + numero2
        print(f'{numero1} + {numero2} = {resultado}')

    elif operacao == '-':
        numero1 = int(input("Digite um número inteiro: "))
        numero2 = int(input("Digite um número inteiro: "))
        resultado = numero1 - numero2
        print(f'{numero1} - {numero2} = {resultado}')

    elif operacao == 'x':
        numero1 = int(input("Digite um número inteiro: "))
        numero2 = int(input("Digite um número inteiro: "))
        resultado = numero1 * numero2
        print(f'{numero1} * {numero2} = {resultado}')

    elif operacao == '/':
        numero1 = int(input("Digite um número inteiro: "))
        numero2 = int(input("Digite um número inteiro: "))
        resultado = numero1 // numero2
        print(f'{numero1} / {numero2} = {resultado}')
    
    elif operacao == "0":
        print("Saindo...")
        print("Calculadora finalizada!")
        break    

    else:
        print("Operação inválida!")

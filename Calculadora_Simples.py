from math import sqrt # importando função raiz quadrada biblioteca math
while True: # Estabelece um loop para que o programa sempre rode até o usuário solicitar a saída
    print("=" * 100)
    print("Calculadora".center(100))
    print("=" * 100)
    print("Menu")
    print("+")
    print("-")
    print("x")
    print("/")
    print("1 - Potenciação")
    print("2 - Raiz quadrada")
    print("3 - Raiz cúbica")
    print("0 - Sair")

    operacao = input("Digite a operação que deseja realizar: ") # Usuário digita uma opção
    
    
    if operacao == '+':     # Realiza a operação soma
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite um número: "))
        resultado = numero1 + numero2
        print(f'{numero1} + {numero2} = {resultado}')

    
    elif operacao == '-':         # Realiza a operação subtração
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite um número: "))
        resultado = numero1 - numero2
        print(f'{numero1} - {numero2} = {resultado}')


    elif operacao == 'x':    # Realiza a operação multiplicação
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite um número: "))
        resultado = numero1 * numero2
        print(f'{numero1} * {numero2} = {resultado}')

    elif operacao == '/':     # Realiza a operação divisão
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite um número: "))
        if numero2 != 0:
            resultado = numero1 // numero2
            print(f'{numero1} / {numero2} = {resultado}')
        else:
            print("Erro! Divisão por zero!")
    

    elif operacao == "1":   # Realiza a operação potenciação
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite um número: "))
        resultado = numero1 ** numero2
        print(f'{numero1}^{numero2} = {resultado}')
    
    
    elif operacao == "2":   # Realiza a operação raiz quadrada
        numero = float(input("Digite um número: "))
        resultado = sqrt(numero)
        print(f'Raiz quadrada de {numero} = {resultado}')

    elif operacao == "3":    # Realiza a operação raiz cúbica
        numero = float(input("Digite um número positivo ou negativo: "))
        if numero >= 0:
            resultado = numero ** (1/3)
            print(f'Raiz cúbica de {numero} = {resultado:.2f}')
        else:
            resultado = -((-numero)) ** (1/3)
            print(f'Raiz cúbica de {numero} = {resultado:.2f}')
    

    elif operacao == "0":    # Realiza a saída do programa
        print("Saindo...")
        print("Calculadora finalizada!")
        break    
    
    else:   # Caso o usuário digite uma opção inválida
        print("Operação inválida!")
        print("Calculadora finalizada!")
        break    
    
    else:   # Caso o usuário digite uma opção inválida
        print("Operação inválida!")

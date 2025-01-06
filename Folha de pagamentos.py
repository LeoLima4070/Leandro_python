import csv
funcionarios = []
while True:
    print("=" * 100)
    print("Sistema de folhas de pagamentos".center(100))
    print("=" * 100)
    print("Menu")
    print("1 - Adicionar novo funcionário")
    print("2 - Buscar funcionário")
    print("3 - Gerar relatório")
    print("4 - Sair")

    def adicionar_funcionario():
        nome_funcionario = input("Digite o nome do funcionário: ")
        matricula = int(input("Digite a matrícula do funcionário: "))
        setor = input("Digite o setor do funcionário: ")
        carga_horaria = int(input("Digite a carga horária do funcionário: "))
        salario_base = float(input("Digite o salário base: R$ "))

        if carga_horaria == 40:
            salario_final = salario_base * 1.2
        elif carga_horaria == 20:
            salario_final = salario_base * 1.1

            for funcionario in funcionarios:
                if funcionario[1] == matricula:
                    print(f'A matrícula {matricula} já possui funcionário cadastrado!')
                    return
        
        funcionarios.append((nome_funcionario, matricula, setor, carga_horaria, salario_base, salario_final))
        print(f'O funcionário {nome_funcionario} com a matrícula {matricula} foi cadastrado com sucesso!')

        with open("Folha_pagamentos.csv", mode="w", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Nome", "Matrícula", "Setor, Carga-Horária, Salário Base"]) 
            for funcionario in funcionarios:
                writer.writerow([[funcionario[0], funcionario[1], funcionario[2]], funcionario[3], funcionario[4]])
            print("Arquivo CSV com funcionários cadastrados criado com sucesso!")


    def buscar_funcionario():
        buscar_matricula = int(input("Digite a matrícula do funcionário que deseja buscar: "))
        for funcionario in funcionarios:
            if funcionario[1] == buscar_matricula:
                print("-" * 100)
                print("Funcionário encontrado".center(100))
                print("-" * 100)
                print(f'Nome: {funcionario[0]}')
                print(f'Matrícula: {funcionario[1]}')
                print(f'Setor: {funcionario[2]}')
                print(f'Carga-Horária: {funcionario[3]} horas')
                print(f'Salário base: R$ {funcionario[4]}')
                print("-" * 100)

    def gerar_relatorio():
        if funcionarios:
            print("-" * 100)
            print("Relatório gerado".center(100))
            print("-" * 100)
            for funcionario in funcionarios:
                print(f'Nome: {funcionario[0]}')
                print(f'Matrícula: {funcionario[1]}')
                print(f'Setor: {funcionario[2]}')
                print(f'Carga-Horária: {funcionario[3]}')
                print(f'Salário base: R$ {funcionario[4]}')
                print(f'Salário final: R$ {funcionario[5]}')
        else:
            print("Não há funcionários cadastrados!")
        
        with open("Folha_pagamentos.csv", mode="w", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Nome", "Matrícula", "Setor, Carga-Horária, Salário Base"]) 
            for funcionario in funcionarios:
                writer.writerow([[funcionario[0], funcionario[1], funcionario[2]], funcionario[3], funcionario[4], funcionario[5]])
            print("Arquivo CSV com funcionários cadastrados criado com sucesso!")


    opcao = int(input("Digite a opção que deseja realizar: "))

    if opcao == 1:
        adicionar_funcionario()
    elif opcao == 2:
        buscar_funcionario()
    elif opcao == 3:
        gerar_relatorio()
    elif opcao == 4:
        print("Saindo...")
        print("Programa finalizado!")
    else:
        print("Opção inválida!")

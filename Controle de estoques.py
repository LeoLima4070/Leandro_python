import csv
produtos = []
while True:
    print("=" * 100)
    print("Estoque de produtos".center(100))
    print("=" * 100)
    print("Menu")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos em estoque")
    print("4 - Criar arquivo")
    print("5 - Sair")

    opcao = int(input("Digite a opção que deseja realizar: "))

    if opcao == 1:
        print("=" * 100)
        print("Adicionar produto".center(100))
        print("=" * 100)
        nome_produto = input("Digite o nome do produto: ").lower()
        codigo_produto = int(input("Digite o código do produto: "))
        Quantidade_produto = int(input("Digite a quantidade de produtos: "))
        
        for produto in produtos:
            if produto[1] == codigo_produto:
                print("Produto com código já cadastrado no sistema!")
                break
        else:
            produtos.append((nome_produto, codigo_produto, Quantidade_produto))
            print(f'Produto {nome_produto} {codigo_produto} cadastrado com sucesso!')

    elif opcao == 2:
        print("=" * 100)
        print("Remover produto".center(100))
        print("=" * 100)
        remover_produto = int(input("Digite o código do produto que deseja remover: "))
        for produto in produtos:
            if produto[1] == remover_produto:
                produtos.remove(produto)
                print(f"O produto {nome_produto} {remover_produto} foi removido com sucesso.")
                break
        else:
            print("Produto não encontrado!")
    
    elif opcao == 3:
        if produtos:
            print("=" * 100)
            print("Produtos em estoque".center(100))
            print("=" * 100)
            for produto in produtos:
                print("-" * 100)
                print(f'Produto: {produto[0].capitalize()}\n')
                print(f'Código: {produto[1]}\n')
                print(f'Quantidade: {produto[2]}\n')
                print("-" * 100)
        else:
            print("Não há produtos registrados no estoque!")
        
    elif opcao == 4:
        with open("Estoque.csv", mode="w", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Nome", "Código", "Quantidade"])  # Cabeçalho do arquivo CSV
            for produto in produtos:
                writer.writerow([produto[0], produto[1], produto[2]])  # Dados dos produtos
            print("Arquivo CSV criado com sucesso!")
    
    elif opcao == 5:
        print("Saindo...")
        print("Programa finalizado!")
        break
    else:
        print("Opção inválida!")

import Funcoes

while True:
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - editar funcionário")
    print("4 - Excluir funcionário")
    print("0 - Encerrar programa")
    opcao = int(input("Informe a opção desejada: "))
    print("\n")

    if (opcao == 1):
        nome = input("Nome do funcionario: ")
        idade = input("Idade do funcionario: ")
        cargo = input("Cargo do funcionario: ")
        salario = input("Salário do funcionario: ")
        Funcoes.adicionar_funcionario(nome, idade, cargo, salario)
        print("\n")
        
    elif (opcao == 2):
        Funcoes.exibir_funcionarios()
        print("\n")
        
    elif (opcao == 3):
        nome = input("Nome do funcionario que deseja alterar: ")
        print("1 - Alterar cargo")
        print("2 - Alterar salario")
        print("3 - Alterar ambos")
        seletor = int(input("Escolha uma opção de alteração: "))
        if (seletor == 1):
            cargo_novo = input("digite o novo cargo: ")
            salario_novo = None
            Funcoes.editar_funcionario(nome, cargo_novo, salario_novo)
            print("\n")
        elif (seletor == 2):
            salario_novo = input("digite o novo salario: ")
            cargo_novo = None
            Funcoes.editar_funcionario(nome, cargo_novo, salario_novo)
            print("\n")
        elif (seletor == 3):
            cargo_novo = input("digite o novo cargo: ")
            salario_novo = input("digite o novo salario: ")
            Funcoes.editar_funcionario(nome, cargo_novo, salario_novo)
            print("\n")
        else:
            break
        
    elif (opcao == 4):
        nome = input("Nome do contato que deseja excluir: ")
        Funcoes.remover_funcionario(nome)
        print("\n")
    
    else:
        break

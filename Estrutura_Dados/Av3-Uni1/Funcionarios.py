# Importação do módulo Funcoes, que contém as funções para manipular os dados dos funcionários
import Funcoes

# Loop principal do programa. O programa continuará em execução até que o usuário decida encerrá-lo
while True:
    # Exibição de um menu com as opções disponíveis para o usuário
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - editar funcionário")
    print("4 - Excluir funcionário")
    print("0 - Encerrar programa")

    # Solicita ao usuário que informe a opção desejada, converte a entrada para um inteiro e armazena na variável 'opcao'
    opcao = int(input("Informe a opção desejada: "))
    print("\n")
    
    # Adicionar um novo funcionário
    if opcao == 1:
        # Solicita os dados do funcionário (nome, idade, cargo e salário)
        nome = input("Nome do funcionário: ")
        idade = input("Idade do funcionário: ")
        cargo = input("Cargo do funcionário: ")
        salario = input("Salário do funcionário: ")
        
        # Chama a função 'adicionar_funcionario' do módulo 'Funcoes' para adicionar o funcionário com os dados fornecidos
        Funcoes.adicionar_funcionario(nome, idade, cargo, salario)
        print("\n")
        
    # Listar todos os funcionários
    elif opcao == 2:
        # Chama a função 'exibir_funcionarios' do módulo 'Funcoes' para listar todos os funcionários cadastrados
        Funcoes.exibir_funcionarios()
        print("\n")

    # Editar dados de um funcionário
    elif opcao == 3:
        # Solicita o nome do funcionário a ser editado
        nome = input("Nome do funcionário que deseja alterar: ")
        
        # Exibe as opções de alteração possíveis (cargo, salário ou ambos)
        print("1 - Alterar cargo")
        print("2 - Alterar salario")
        print("3 - Alterar ambos")
        
        # Solicita ao usuário que escolha qual dado do funcionário deseja alterar
        seletor = int(input("Escolha uma opção de alteração: "))
        
        # Caso o usuário escolha alterar apenas o cargo
        if seletor == 1:
            cargo_novo = input("digite o novo cargo: ")  # Solicita o novo cargo
            salario_novo = None  # O salário não será alterado, então é atribuído None
            
            # Chama a função 'editar_funcionario' passando o nome do funcionário e o novo cargo
            Funcoes.editar_funcionario(nome, cargo_novo, salario_novo)
            print("\n")

        # Caso o usuário escolha alterar apenas o salário
        elif seletor == 2:
            salario_novo = input("digite o novo salario: ")  # Solicita o novo salário
            cargo_novo = None  # O cargo não será alterado, então é atribuído None
            
            # Chama a função 'editar_funcionario' passando o nome do funcionário e o novo salário
            Funcoes.editar_funcionario(nome, cargo_novo, salario_novo)
            print("\n")

        # Caso o usuário escolha alterar ambos os dados (cargo e salário)
        elif seletor == 3:
            cargo_novo = input("digite o novo cargo: ")  # Solicita o novo cargo
            salario_novo = input("digite o novo salario: ")  # Solicita o novo salário
            
            # Chama a função 'editar_funcionario' passando o nome do funcionário, novo cargo e novo salário
            Funcoes.editar_funcionario(nome, cargo_novo, salario_novo)
            print("\n")

        # Caso o usuário forneça uma opção inválida, o loop é encerrado
        else:
            break

    # Excluir um funcionário
    elif opcao == 4:
        # Solicita o nome do funcionário a ser excluído
        nome = input("Nome do funcionário que deseja excluir: ")
        
        # Chama a função 'remover_funcionario' do módulo 'Funcoes' para excluir o funcionário
        Funcoes.remover_funcionario(nome)
        print("\n")
        
    # Caso o usuário escolha a opção 0, o programa será encerrado
    else:
        break  # Encerra o loop e termina o programa

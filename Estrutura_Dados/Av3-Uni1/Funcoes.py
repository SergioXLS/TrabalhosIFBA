# Função para adicionar um novo funcionário ao arquivo "funcionarios.txt"
def adicionar_funcionario(nome, idade, cargo, salario):
    # Abre o arquivo "funcionarios.txt" no modo de adição ("a"), permitindo adicionar novos dados sem sobrescrever os existentes
    with open("funcionarios.txt", "a") as arquivo: # utiliza um with para garantir que o arquivo seja fechado corretamente
        # Escreve os dados do novo funcionário no formato "nome;idade;cargo;salário", seguidos de uma nova linha
        arquivo.write(nome + ";" + idade + ";" + cargo + ";" + salario + "\n")
        
# Função para exibir todos os funcionários cadastrados no arquivo "funcionarios.txt"
def exibir_funcionarios():
    # Abre o arquivo "funcionarios.txt" no modo de leitura ("r")
    with open("funcionarios.txt", "r") as arquivo: # utiliza um with para garantir que o arquivo seja fechado corretamente
        # Exibe um título formatado para a seção de funcionários
        print("================================")
        print("          FUNCIONÁRIOS          ")
        print("================================\n")
        
        # Lê todas as linhas do arquivo e itera sobre elas
        for linha in arquivo.readlines():
            # Remove o caractere de nova linha e divide a linha usando ";" como delimitador
            valores = linha.strip().split(";")
            # Exibe os dados de cada funcionário, com base nos valores extraídos
            print("Nome:", valores[0])
            print("Idade:", valores[1])
            print("Cargo:", valores[2])
            print("Salário:", valores[3])
            # Exibe uma linha separadora após os dados do funcionário
            print("================================")
            
# Função para editar os dados de um funcionário no arquivo "funcionarios.txt"
def editar_funcionario(nome, cargo_novo, salario_novo):
    # Abre o arquivo "funcionarios.txt" no modo de leitura ("r") e lê todas as linhas
    with open("funcionarios.txt", "r") as arquivo: # utiliza um with para garantir que o arquivo seja fechado corretamente
        conteudo = arquivo.readlines()

    # Abre o arquivo novamente, mas agora no modo de escrita ("w"), sobrescrevendo o conteúdo original
    with open("funcionarios.txt", "w") as arquivo:
        # Itera sobre as linhas lidas anteriormente
        for linha in conteudo:
            # Remove o caractere de nova linha e divide a linha usando ";" como delimitador
            dados = linha.replace('\n', '').split(";")
            # Verifica se o nome do funcionário na linha corresponde ao nome informado
            if dados[0] == nome:
                # Se um novo cargo foi fornecido, substitui o cargo atual
                if cargo_novo != None:
                    dados[2] = cargo_novo
                # Se um novo salário foi fornecido, substitui o salário atual
                if salario_novo != None:
                    dados[3] = salario_novo
                # Escreve a linha modificada de volta no arquivo, com os dados atualizados
                arquivo.write(dados[0] + ";" + dados[1] + ";" + dados[2] + ";" + dados[3] + "\n")
            else:
                # Caso o nome não corresponda, escreve a linha original no arquivo
                arquivo.write(linha)
                
# Função para remover um funcionário do arquivo "funcionarios.txt"
def remover_funcionario(nome):
    # Abre o arquivo "funcionarios.txt" no modo de leitura ("r") e lê todas as linhas
    with open("funcionarios.txt", "r") as arquivo: # utiliza um with para garantir que o arquivo seja fechado corretamente
        conteudo = arquivo.readlines()

    # Abre o arquivo novamente no modo de escrita ("w") para sobrescrever o conteúdo
    with open("funcionarios.txt", "w") as arquivo:
        # Itera sobre as linhas lidas anteriormente
        for linha in conteudo:
            # Remove o caractere de nova linha e divide a linha usando ";" como delimitador
            dados = linha.replace('\n', '').split(";")
            # Verifica se o nome do funcionário na linha é diferente do nome informado
            if dados[0] != nome:
                # Se o nome não for o mesmo, escreve a linha no arquivo
                arquivo.write(dados[0] + ";" + dados[1] + ";" + dados[2] + ";" + dados[3] + "\n")

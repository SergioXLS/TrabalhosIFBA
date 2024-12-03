def adicionar_funcionario(nome, idade, cargo, salario):
    with open("funcionarios.txt", "a") as arquivo:
        arquivo.write(nome + ";" + idade + ";" + cargo + ";" + salario + "\n")
        
def exibir_funcionarios():
    with open("funcionarios.txt", "r") as arquivo:
        print("================================")
        print("          FUNCIONÁRIOS          ")
        print("================================\n")
        for linha in arquivo.readlines():
            valores = linha.strip().split(";")
            print("Nome:", valores[0])
            print("Idade:", valores[1])
            print("Cargo:", valores[2])
            print("Salário:", valores[3])
            print("================================")
            
def editar_funcionario(nome, cargo_novo, salario_novo):
    with open("funcionarios.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    with open("funcionarios.txt", "w") as arquivo:
        for linha in conteudo:
            dados = linha.replace('\n', '').split(";")
            if dados[0] == nome:
                if cargo_novo != None:
                    dados[2] = cargo_novo
                if salario_novo != None:
                    dados[3] = salario_novo
                arquivo.write(dados[0] + ";" + dados[1] + ";" + dados[2] + ";" + dados[3] + "\n")
            else:
                arquivo.write(linha)
                
def remover_funcionario(nome):
    with open("funcionarios.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    with open("funcionarios.txt", "w") as arquivo:
        for linha in conteudo:
            dados = linha.replace('\n', '').split(";")
            if dados[0] != nome:
                arquivo.write(dados[0] + ";" + dados[1] + ";" + dados[2] + ";" + dados[3] + "\n")

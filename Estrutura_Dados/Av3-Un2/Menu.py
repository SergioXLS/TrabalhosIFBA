from Biblioteca import Biblioteca

def menu_principal():
    print("\n=== SISTEMA DE BIBLIOTECA DIGITAL ===")
    print("1. Ordenar livros")
    print("2. Buscar livro por ISBN")
    print("3. Comparar algoritmos")
    print("4. Sair")
    return input("Escolha uma opção: ")

def menu_ordenacao():
    print("\nCritérios de ordenação:")
    print("1. Título")
    print("2. Autor")
    print("3. Ano")
    criterio = input("Escolha o critério: ")
    
    print("\nAlgoritmos de ordenação:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    algoritmo = input("Escolha o algoritmo: ")
    
    return criterio, algoritmo

def menu_busca():
    print("\nAlgoritmos de busca:")
    print("1. Busca Linear")
    print("2. Busca Binária")
    algoritmo = input("Escolha o algoritmo: ")
    
    isbn = input("Digite o ISBN a ser buscado: ")
    
    return algoritmo, isbn

def menu_comparacao():
    print("\nComparar algoritmos:")
    print("1. Comparar algoritmos de ordenação")
    print("2. Comparar algoritmos de busca")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        print("\nCritérios de ordenação:")
        print("1. Título")
        print("2. Autor")
        print("3. Ano")
        criterio = input("Escolha o critério: ")
        
        algoritmos = []
        print("\nSelecione os algoritmos para comparar (digite os números separados por vírgula):")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        escolhas = input("Escolha os algoritmos: ").split(',')
        
        for escolha in escolhas:
            if escolha.strip() == '1':
                algoritmos.append(('bubble', 'Bubble Sort'))
            elif escolha.strip() == '2':
                algoritmos.append(('selection', 'Selection Sort'))
            elif escolha.strip() == '3':
                algoritmos.append(('insertion', 'Insertion Sort'))
            elif escolha.strip() == '4':
                algoritmos.append(('merge', 'Merge Sort'))
            elif escolha.strip() == '5':
                algoritmos.append(('quick', 'Quick Sort'))
        
        return 'ordenacao', criterio, algoritmos
    
    elif opcao == '2':
        algoritmos = []
        print("\nSelecione os algoritmos para comparar (digite os números separados por vírgula):")
        print("1. Busca Linear")
        print("2. Busca Binária")
        escolhas = input("Escolha os algoritmos: ").split(',')
        
        for escolha in escolhas:
            if escolha.strip() == '1':
                algoritmos.append(('linear', 'Busca Linear'))
            elif escolha.strip() == '2':
                algoritmos.append(('binary', 'Busca Binária'))
        
        isbn = input("Digite o ISBN a ser buscado (ou deixe em branco para um aleatório): ")
        return 'busca', isbn, algoritmos
    
    return None, None, None
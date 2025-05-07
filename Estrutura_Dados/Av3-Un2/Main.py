from Biblioteca import Biblioteca
from Menu import *
import time, random


def main():
    biblioteca = Biblioteca()
    biblioteca.carregar_livros('livros.txt')
    
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            criterio_num, algoritmo_num = menu_ordenacao()
            
            criterios = {'1': 'titulo', '2': 'autor', '3': 'ano'}
            algoritmos = {
                '1': ('bubble', 'Bubble Sort'),
                '2': ('selection', 'Selection Sort'),
                '3': ('insertion', 'Insertion Sort'),
                '4': ('merge', 'Merge Sort'),
                '5': ('quick', 'Quick Sort')
            }
            
            criterio = criterios.get(criterio_num, 'titulo')
            algoritmo, nome_algoritmo = algoritmos.get(algoritmo_num, ('bubble', 'Bubble Sort'))
            
            inicio = time.time()
            biblioteca.reset_comparacoes()
            
            if algoritmo == 'bubble':
                biblioteca.bubble_sort(criterio)
            elif algoritmo == 'selection':
                biblioteca.selection_sort(criterio)
            elif algoritmo == 'insertion':
                biblioteca.insertion_sort(criterio)
            elif algoritmo == 'merge':
                biblioteca.merge_sort(criterio)
            elif algoritmo == 'quick':
                biblioteca.quick_sort(criterio)
            
            tempo = time.time() - inicio
            
            print(f"\nOrdenação concluída com {nome_algoritmo} por {criterio}.")
            print(f"Tempo de execução: {tempo:.6f} segundos")
            print(f"Número de comparações: {biblioteca.comparacoes}")
            
            # Mostrar os primeiros 5 livros ordenados
            print("\nPrimeiros 5 livros ordenados:")
            for livro in biblioteca.livros[:5]:
                print(livro)
        
        elif opcao == '2':
            algoritmo_num, isbn = menu_busca()
            
            algoritmos = {
                '1': ('linear', 'Busca Linear'),
                '2': ('binary', 'Busca Binária')
            }
            
            algoritmo, nome_algoritmo = algoritmos.get(algoritmo_num, ('linear', 'Busca Linear'))
            
            inicio = time.time()
            biblioteca.reset_comparacoes()
            
            if algoritmo == 'linear':
                posicao = biblioteca.busca_linear(isbn)
            elif algoritmo == 'binary':
                # Ordenar por ISBN primeiro para busca binária
                biblioteca.quick_sort('isbn')
                posicao = biblioteca.busca_binaria(isbn)
            
            tempo = time.time() - inicio
            
            if posicao != -1:
                print(f"\nLivro encontrado na posição {posicao}:")
                print(biblioteca.livros[posicao])
            else:
                print("\nLivro não encontrado.")
            
            print(f"\nBusca concluída com {nome_algoritmo}.")
            print(f"Tempo de execução: {tempo:.6f} segundos")
            print(f"Número de comparações: {biblioteca.comparacoes}")
        
        elif opcao == '3':
            tipo, criterio_isbn, algoritmos = menu_comparacao()
            
            if tipo == 'ordenacao':
                criterios = {'1': 'titulo', '2': 'autor', '3': 'ano'}
                criterio = criterios.get(criterio_isbn, 'titulo')
                
                print(f"\nComparando algoritmos de ordenação por {criterio}:")
                print("{:<15} {:<20} {:<15}".format("Algoritmo", "Tempo (segundos)", "Comparações"))
                print("-" * 50)
                
                for algo, nome in algoritmos:
                    tempo, comp = biblioteca.ordenar_e_medir(algo, criterio)
                    print("{:<15} {:<20.6f} {:<15}".format(nome, tempo, comp))
            
            elif tipo == 'busca':
                if not criterio_isbn.strip():
                    # Escolher um livro aleatório para busca
                    livro_aleatorio = random.choice(biblioteca.livros)
                    isbn = livro_aleatorio.isbn
                    print(f"\nBuscando por ISBN aleatório: {isbn}")
                else:
                    isbn = criterio_isbn
                
                print("\nComparando algoritmos de busca:")
                print("{:<15} {:<20} {:<15} {:<15}".format("Algoritmo", "Tempo (segundos)", "Comparações", "Encontrado?"))
                print("-" * 70)
                
                for algo, nome in algoritmos:
                    tempo, comp, encontrado = biblioteca.buscar_e_medir(algo, isbn)
                    print("{:<15} {:<20.6f} {:<15} {:<15}".format(
                        nome, tempo, comp, "Sim" if encontrado else "Não"))
        
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

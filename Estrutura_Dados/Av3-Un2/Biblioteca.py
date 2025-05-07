from Livro import Livro
import time

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.comparacoes = 0
    
    def carregar_livros(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as arq:
            linhas = arq.readlines()
            for linha in linhas[1:]:
                dados = linha.strip().split(';')
                if len(dados) == 5:
                    livro = Livro(*dados)
                    self.livros.append(livro)
                    
    def reset_comparacoes(self):
        self.comparacoes = 0
    
    def bubble_sort(self, criterio):
        n = len(self.livros)
        for i in range(n):
            for j in range(0, n-i-1):
                self.comparacoes += 1
                l1 = getattr(self.livros[j], criterio)
                l2 = getattr(self.livros[j+1], criterio)
                if l1 > l2:
                    self.livros[j], self.livros[j+1] = self.livros[j+1], self.livros[j]
    
    def selection_sort(self, criterio):
        n = len(self.livros)
        for i in range(n):
            menor = i
            for j in range(i+1, n):
                self.comparacoes += 1
                l1 = getattr(self.livros[j], criterio)
                l2 = getattr(self.livros[menor], criterio)
                if l1 < l2:
                    menor = j
            self.livros[i], self.livros[menor] = self.livros[menor], self.livros[i]
    
    def insertion_sort(self, criterio):
        for i in range(1, len(self.livros)):
            chave = self.livros[i]
            j = i-1
            
            while j >= 0:
                self.comparacoes += 1
                if getattr(chave, criterio) < getattr(self.livros[j], criterio):
                    self.livros[j+1] = self.livros[j]
                    j -= 1
                else:
                    break
                
            self.livros[j+1] = chave
    
    def merge_sort(self, criterio, livros=None):
        if livros is None:
            livros = self.livros
        
        if len(livros) > 1:
            meio = len(livros) // 2
            esquerda = livros[:meio]
            direita = livros[meio:]

            self.merge_sort(criterio, esquerda)
            self.merge_sort(criterio, direita)

            i = j = y = 0

            while i < len(esquerda) and j < len(direita):
                self.comparacoes += 1
                if getattr(esquerda[i], criterio) <= getattr(direita[j], criterio):
                    livros[y] = esquerda[i]
                    i += 1
                else:
                    livros[y] = direita[j]
                    j += 1
                y += 1

            while i < len(esquerda):
                livros[y] = esquerda[i]
                i += 1
                y += 1

            while j < len(direita):
                livros[y] = direita[j]
                j += 1
                y += 1
    
    def sel_pivo(self, arr, inicio, fim, criterio):
        pivo = arr[fim]
        i = inicio - 1
        
        for j in range(inicio, fim):
            self.comparacoes += 1
            if getattr(arr[j], criterio) <= getattr(pivo, criterio):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[fim] = arr[fim], arr[i+1]
        return i + 1

    def quick_sort_helper(self, arr, inicio, fim, criterio):
        if inicio < fim:
            pi = self.sel_pivo(arr, inicio, fim, criterio)
            self.quick_sort_helper(arr, inicio, pi-1, criterio)
            self.quick_sort_helper(arr, pi+1, fim, criterio)

    def quick_sort(self, criterio):
        self.quick_sort_helper(self.livros, 0, len(self.livros)-1, criterio)
    
    def busca_linear(self, isbn):
        for i, livro in enumerate(self.livros):
            self.comparacoes += 1
            if livro.isbn == isbn:
                return i
        return -1
    
    def busca_binaria(self, isbn):
        esq = 0
        dir = len(self.livros) - 1
        
        while esq <= dir:
            self.comparacoes += 1
            meio = (esq + dir) // 2
            if self.livros[meio].isbn == isbn:
                return meio
            elif self.livros[meio].isbn < isbn:
                esq = meio + 1
            else:
                dir = meio - 1
        return -1
    
    def ordenar_e_medir(self, algoritmo, criterio):
        self.reset_comparacoes()
        copia_livros = self.livros.copy()
        
        inicio = time.time()
        
        if algoritmo == 'bubble':
            self.bubble_sort(criterio)
        elif algoritmo == 'selection':
            self.selection_sort(criterio)
        elif algoritmo == 'insertion':
            self.insertion_sort(criterio)
        elif algoritmo == 'merge':
            self.merge_sort(criterio)
        elif algoritmo == 'quick':
            self.quick_sort(criterio)
        
        tempo = time.time() - inicio

        self.livros = copia_livros
        
        return tempo, self.comparacoes
    
    def buscar_e_medir(self, algoritmo, isbn):
        self.reset_comparacoes()
        copia_livros = self.livros.copy()
        
        inicio = time.time()
        
        if algoritmo == 'linear':
            resultado = self.busca_linear(isbn)
        elif algoritmo == 'binary':
            self.quick_sort('isbn')
            resultado = self.busca_binaria(isbn)
        
        tempo = time.time() - inicio
        
        self.livros = copia_livros
        
        return tempo, self.comparacoes, resultado != -1
from Livros import Livros

class ordenar_livros:
    
    @staticmethod
    def bubble_sort(livros, atributo='titulo'):
        i = len(livros)
        for x in range(i):
            for y in range(0, i-x-1):
                if getattr(livros[y], atributo) > getattr(livros[y+1], atributo):
                    livros[y], livros[y+1] = livros[y+1], livros[y]
        return livros
    
    @staticmethod
    def selection_sort(livros, atributo='titulo'):
        i = len(livros)
        for x in range(i):
            menor = x
            for y in range(x+1, i):
                if getattr(livros[y], atributo) < getattr(livros[menor], atributo):
                    menor = y
            livros[x], livros[menor] = livros[menor], livros[x]
        return livros
    
    @staticmethod
    def insertion_sort(livros, atributo='ISBN'):
        for i in range(1, len(livros)):
            chave = livros[i]
            x = i-1
            while x >= 0 and getattr(livros[x], atributo) > getattr(chave, atributo):
                livros[x+1] = livros[x]
                x -= 1
            livros[x+1] = chave
        return livros
    
    @staticmethod
    def merge_sort(livros, atributo='ISBN'):
        if len(livros) > 1:
            return livros
        meio = len(livros) // 2
        esquerda = (livros[:meio]) # Ordenar a metade esquerda
        direita = (livros[meio:])
        ordenar_livros.merge_sort(esquerda, atributo)
        ordenar_livros.merge_sort(direita, atributo)
    
        i = x = y = 0
        while i < len(esquerda) and x < len(direita):
            if getattr(esquerda[i], atributo) <= getattr(direita[x], atributo):
                livros[y] = esquerda[i]
                i += 1
            else:
                livros[y] = direita[i]
                i += 1
            y += 1

        while i < len(esquerda):
            livros[y] = esquerda[i]
            i += 1
            y += 1

        while x < len(direita):
            livros[y] = direita[x]
            x += 1
            y += 1
        return livros
    
    @staticmethod
    def quick_sort(livros, atributo='ISBN'):
        if len(livros) <= 1:
            return livros
        else:
            pivo = getattr(livros[-1])
            menores = [x for x in getattr(livros[:-1]) if x <= pivo]
            maiores = [x for x in getattr(livros[:-1]) if x > pivo]
            return ordenar_livros.quick_sort(menores) + [pivo] + ordenar_livros.quick_sort(maiores)
        
        menores, maiores = [], []
        if len(livros) <= 1:
            return livros
        else:
            pivo = getattr(livros[-1])
            for x in range(len(livros)-1):
                if getattr(livros[x] < pivo):
                    menores.append(livros[x])
                else:
                    maiores.append(livros[x])
            return ordenar_livros.quick_sort(menores) + [pivo] + ordenar_livros.quick_sort(maiores)
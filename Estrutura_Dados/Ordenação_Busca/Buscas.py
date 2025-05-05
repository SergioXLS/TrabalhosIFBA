from Livros import Livros

class Buscar_livros:
    
    @staticmethod
    def busca_linear(livros, chave, atributo='ISBN'):
        for livro in livros:
            if getattr(livro, atributo) == chave:
                return livro
        return None
    
    @staticmethod
    def busca_binaria(livros, chave, atributo='ISBN'):
        inicio = 0
        fim = len(livros) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            valor_meio = getattr(livros[meio], atributo)
            if valor_meio == chave:
                return livros[meio]
            elif valor_meio < chave:
                inicio = meio + 1
            else:
                fim = meio - 1  
        return None
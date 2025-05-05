class Livros:

    def __init__(self, ISBN, titulo, autor, paginas, ano):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.paginas = int(paginas)
        self.ano = int(ano)
    
    def __str__(self):
        return f'{self.ISBN}, {self.titulo}, {self.autor}, {self.paginas}, {self.ano}'

    def preencher_lista():
        livros = []
        with open(livros.txt, 'r') as arquivo:
            for linha in arquivo:
                valores = linha.strip().split(";")
                if len(valores) == 5:
                    ISBN, titulo, autor, paginas, ano = valores
                    livro = Livros(ISBN, titulo, autor, paginas, ano)
                    livros.append(livro)
        return livros

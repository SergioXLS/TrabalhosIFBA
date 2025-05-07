class Livro:

    def __init__(self, isbn, titulo, autor, paginas, ano ):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.paginas = int(paginas)
        self.ano = int(ano)
    
    def __str__(self):
        return f"ISBN: {self.isbn}, Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}, Ano: {self.ano}"
    
    def __repr__(self):
        return self.__str__()
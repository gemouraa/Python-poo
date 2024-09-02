import os 

os.system("cls || clear")

class Livro:
    def __init__(self, titulo, autor, numeroPaginas, preco) -> None:
        self.titulo = titulo
        self.autor = autor
        self.numeroPaginas = numeroPaginas
        self.preco = preco
        
    def exibirDados(self) -> str:
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nNumero de Paginas {self.numeroPaginas} \nPreço {self.preco}"
    
livro = Livro("Neymar 2011", "Neymar Pai", 2015, "222M")

print(livro.exibirDados())

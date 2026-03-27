class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class CatalogoLivraria:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def buscar_por_titulo(self, titulo_buscado):
        # Refatoração: Busca ignorando maiúsculas/minúsculas e aceitando partes do título
        termo = titulo_buscado.lower()
        return [
            livro for livro in self.acervo 
            if termo in livro.titulo.lower()
        ]
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
        # Código mínimo para passar no teste
        resultados = []
        for livro in self.acervo:
            if livro.titulo == titulo_buscado:
                resultados.append(livro)
        return resultados
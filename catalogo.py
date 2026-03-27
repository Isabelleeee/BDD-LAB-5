class Livro:
    # Atualizado com o preço
    def __init__(self, titulo, autor, ano, categoria="", preco=0.0):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.preco = preco
        
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
    def buscar_por_autor(self, autor_buscado):
        # Refatorado: Busca flexível ignorando maiúsculas/minúsculas
        termo = autor_buscado.lower()
        return [
            livro for livro in self.acervo 
            if termo in livro.autor.lower()
        ]
    def ordenar_por_preco(self):
        # Refatorado: usa a função nativa do Python para ordenar a lista baseada no atributo preco
        return sorted(self.acervo, key=lambda livro: livro.preco)
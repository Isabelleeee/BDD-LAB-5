import unittest
from catalogo import Livro, CatalogoLivraria

class TestComportamentoBuscaCatalogo(unittest.TestCase):
    def setUp(self):
        # DADO que o catálogo possui os livros "1984" e "O Hobbit"
        self.catalogo = CatalogoLivraria()
        self.catalogo.adicionar_livro(Livro("1984", "George Orwell", 1949))
        self.catalogo.adicionar_livro(Livro("O Hobbit", "J.R.R. Tolkien", 1937))

    def test_quando_busca_titulo_existente_entao_retorna_livro(self):
        # QUANDO o usuário busca pelo título "1984"
        resultados = self.catalogo.buscar_por_titulo("1984")
        
        # ENTÃO o sistema deve retornar o livro "1984"
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].titulo, "1984")

    def test_quando_busca_titulo_inexistente_entao_retorna_vazio(self):
        # QUANDO o usuário busca pelo título "Fundação"
        resultados = self.catalogo.buscar_por_titulo("Fundação")
        
        # ENTÃO o sistema deve retornar uma lista vazia
        self.assertEqual(len(resultados), 0)
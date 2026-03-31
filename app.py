import streamlit as st
from catalogo import CatalogoLivraria, Livro

# 1. Configurando o catálogo inicial simulado (DADO)
@st.cache_data
def carregar_catalogo():
    cat = CatalogoLivraria()
    # Adicionando os livros do seu teste e mais alguns para podermos ver a interface funcionando
    cat.adicionar_livro(Livro("1984", "George Orwell", 1949, "Ficção", 39.90))
    cat.adicionar_livro(Livro("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia", 49.90))
    cat.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia", 120.00))
    cat.adicionar_livro(Livro("Livro Barato", "Autor B", 2021, "TI", 15.00))
    cat.adicionar_livro(Livro("Livro Caro", "Autor A", 2020, "TI", 150.00))
    return cat

catalogo = carregar_catalogo()

# 2. A Interface Visual
st.title("📚 Livraria BDD")
st.write("Teste do MVP rodando integrado com o backend em Python.")

# Menu lateral para interação do usuário (QUANDO)
with st.sidebar:
    st.header("🔍 Filtros de Busca")
    
    # Entradas de texto
    busca_titulo = st.text_input("Buscar por Título:")
    busca_autor = st.text_input("Buscar por Autor:")
    
    st.divider()
    # O botão de ordenar que usa o seu método específico
    ordenar = st.checkbox("Ordenar por Preço (Menor para o Maior)")

# 3. Lógica de integração com o seu catalogo.py
# Pega o catálogo inteiro ou já chama o seu método de ordenação
if ordenar:
    resultados = catalogo.ordenar_por_preco()
else:
    resultados = catalogo.acervo

# Aplica as buscas se o usuário digitou algo
if busca_titulo:
    # Usando a mesma lógica do seu método buscar_por_titulo
    resultados = [livro for livro in resultados if busca_titulo.lower() in livro.titulo.lower()]

if busca_autor:
    # Usando a mesma lógica do seu método buscar_por_autor
    resultados = [livro for livro in resultados if busca_autor.lower() in livro.autor.lower()]

# 4. Exibindo os Resultados na Tela (ENTÃO)
st.subheader(f"Encontramos {len(resultados)} livro(s):")

# Criando "cards" visuais para cada livro filtrado
for livro in resultados:
    # Dividindo em colunas para a interface ficar com cara de aplicativo
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"### 📖 {livro.titulo}")
        st.write(f"**Autor:** {livro.autor} | **Ano:** {livro.ano} | **Categoria:** {livro.categoria}")
    
    with col2:
        st.markdown(f"### R$ {livro.preco:.2f}")
        # O botão do MVP direcionando para o "WhatsApp"
        st.button("Comprar via WhatsApp", key=livro.titulo)
    
    st.divider()
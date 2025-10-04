# 🧪 Teste para Analytics — Luiz Henrique

Este projeto foi desenvolvido em **Python** para simular e analisar dados de vendas de uma farmácia fictícia.

## 📌 Descrição do Projeto

- **`limpeza_dados.py`** → Arquivo principal responsável por gerar os dados fictícios.  
  - A farmácia possui **21 produtos** cadastrados.  
  - Foram gerados **720 registros**, sendo **60 registros por mês em 2023**.  

- **`analise_dos_dados.ipynb`** → Notebook utilizado para:  
  - Tratar duplicatas.  
  - Identificar os produtos mais vendidos.  
  - Produzir gráficos.  
  - Cadastrar os resultados do `data_clean.csv` em um banco de dados **SQLite3**.  

- **`consultas.sql`** → Arquivo contendo as consultas SQL exigidas no desafio.  

- **`dbvendas`** → Banco de dados gerado pela célula responsável pelo BD no notebook.  

- **`requirements.txt`** → Lista de dependências necessárias para rodar o projeto.  

## ⚙️ Requisitos

Instale as dependências com:

```bash
pip install -r requirements.txt

```

## 🏗️ Estrutura do Código — `limpeza_dados.py`

No arquivo `limpeza_dados.py` temos duas classes principais:

### 🔹 Classe `Produto`
Representa os produtos da farmácia, com os seguintes atributos:
- `id` → identificador único.  
- `nome` → nome do produto.  
- `categoria` → categoria do produto.  
- `preco` → preço unitário.  

### 🔹 Classe `Dados`
Representa os registros de vendas, com os seguintes atributos:
- `id` → identificador único do registro.  
- `data` → data da venda.  
- `produto` → instância da classe `Produto`.  
- `quantidade` → quantidade vendida.  

### 🔹 Função `montar_dados()`
- Instancia **21 produtos diferentes**.  
- Cria **720 objetos `Dados`**, sendo **60 registros por mês**.  
- Retorna uma lista com **12 listas internas**, uma para cada mês de 2023:  
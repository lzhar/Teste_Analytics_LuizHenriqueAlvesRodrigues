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
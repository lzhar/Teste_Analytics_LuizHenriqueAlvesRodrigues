# 🧪 Teste para Analytics — Luiz Henrique

Este projeto foi desenvolvido em **Python** para simular e analisar dados de vendas de uma farmácia fictícia.
As bibliotecas utilizadas foram  🐼 **Pandas**, 🧮**matplotlib**, 🗄️**sqlite3** e 📄**csv**

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

### Função `montar_data_set()`

A função `montar_data_set` inicia com **registros de segurança**, garantindo que qualquer dado faltante seja corrigido antes de montar o dataset mensal.  

### Produtos de Emergência

```
produto1 = Produto(1, "", "Medicamentos", 7.5000)
produto2 = Produto(2, "Dipirona 500mg", "Medicamentos", 5.9090)
produto3 = Produto(3, "Ibuprofeno 400mg", "Medicamentos", 8.9098)
produto4 = Produto(4, "Sabonete Lux", "Produtos de higiene pessoal", 3.5013)
produto5 = Produto(5, "Shampoo Seda", "Produtos de higiene pessoal", 9.9543)
produto6 = Produto(6, "Creme Dental Colgate", "Produtos de higiene pessoal", 6.95098)
produto7 = Produto(7, "Batom Maybelline", "Produtos de beleza", 29.9012)
produto8 = Produto(8, "Base Vult", "Produtos de beleza", 35.9032)
produto9 = Produto(9, "Perfume Natura", "Produtos de beleza", 89.993232)
produto10 = Produto(10, "Multivitamínico Centrum", "Produtos de bem-estar", 29.9099)
produto11 = Produto(11, "Ômega 3 Sundown", "Produtos de bem-estar", 49.90332)
produto12 = Produto(12, "Chá de Camomila", "Produtos de bem-estar", 4.9012)
produto13 = Produto(13, "Fralda Pampers Confort Sec G", "Produtos para bebês", 189.9032)
produto14 = Produto(14, "Lenço Umedecido Huggies", "Produtos para bebês", 9.90323)
produto15 = Produto(15, "Fórmula Infantil Nan", "Produtos para bebês", 39.90323)
produto16 = Produto(16, "Gaze Estéril", "Produtos hospitalares e de primeiros socorros", 6.90213)
produto17 = Produto(17, "Álcool 70%", "Produtos hospitalares e de primeiros socorros", 3.903232)
produto18 = Produto(18, "Termômetro Digital", "Produtos hospitalares e de primeiros socorros", 45.9032)
produto19 = Produto(19, "Chocolate Snickers", "Produtos de conveniência", 5.49233)
produto20 = Produto(20, "Biscoito Oreo", "Produtos de conveniência", 6.90323)
produto21 = Produto(21, "Suco de Laranja Del Valle", "Produtos de conveniência", 4.90323)

``` 

## 📊 Estrutura do Dataset

O dataset é declarado como um **dicionário**, onde cada chave corresponde a um mês 🗓️ (`"janeiro"`, `"fevereiro"`, etc.) e cada valor é uma lista com **60 registros** 📝.

# Tratamento de Dados Faltantes

Este é um exemplo de como o tratamento funciona: a função verifica se há alguma informação faltante em cada registro.  
Se houver, o dado é preenchido e, após o tratamento, é adicionado à lista correspondente (`append`).  
Ao final, a função retorna o `dataset_vendas_meses`, que contém **60 registros de vendas por mês** 🗓️📝.

```
while(contador < 720):
    if contador >= 0 and contador <= 59:

        if(dataset_vendas_meses["janeiro"][contador_interno].produto.nome == "" 
           or dataset_vendas_meses["janeiro"][contador_interno].produto.nome == " "):
            for item in lista_de_emergencia_produtos:
                if dataset_vendas_meses["janeiro"][contador_interno].produto.id == item.id:
                    dataset_vendas_meses["janeiro"][contador_interno].produto.nome = item.nome
                    break

        if(dataset_vendas_meses["janeiro"][contador_interno].produto.categoria == "Não consta" 
           or dataset_vendas_meses["janeiro"][contador_interno].produto.categoria == " "):
            for item in lista_de_emergencia_produtos:
                if dataset_vendas_meses["janeiro"][contador_interno].produto.id == item.id:
                    dataset_vendas_meses["janeiro"][contador_interno].produto.categoria = item.categoria
                    break

        if (dataset_vendas_meses["janeiro"][contador_interno].produto.preco == 0):
            for item in lista_de_emergencia_produtos:
                if dataset_vendas_meses["janeiro"][contador_interno].produto.id == item.id:
                    self.formatar_numero(item.preco)
                    dataset_vendas_meses["janeiro"][contador_interno].produto.preco = item.preco
                    break

        precoDefinitivo = self.formatar_numero(
            dataset_vendas_meses["janeiro"][contador_interno].produto.preco
        )
        dataset_vendas_meses["janeiro"][contador_interno].produto.preco = precoDefinitivo
        dados_janeiro_tratados.append(dataset_vendas_meses["janeiro"][contador_interno])
        contador_interno += 1

```


## 🔢 Função `formatar_numero()`

A função `formatar_numero()` recebe um **número** como parâmetro e é utilizada para **padronizar os valores de preço**.  
Ela retorna o valor já formatado com o número adequado de casas decimais.

### Exemplos

```python
entrada = 9.9323232
saida = formatar_numero(entrada)  # saída -> 9.93

entrada = 9.9098899888
saida = formatar_numero(entrada)  # saída -> 9.9

```

## 🗂️ Função `dados_para_dict()`

A função `dados_para_dict()` retorna um **dicionário padronizado** com os atributos de um objeto de dados.  
Esse dicionário pode ser utilizado para **exportar os dados para um CSV** em outra função.

### Corpo da função

```python
return {
    "id": obj.id,
    "data": obj.data,
    "produto_nome": obj.produto.nome,
    "produto_categoria": obj.produto.categoria,
    "produto_preco": obj.produto.preco,
    "quantidade": obj.quantidade
}
```


## 📝 Função `montar_csv()`

A função `montar_csv()` utiliza a biblioteca **pandas** para criar um **CSV** a partir dos dados retornados pela função `dados_para_dict()`.  
Ao final, gera o arquivo chamado **`data_clean.csv`** contendo todos os registros padronizados.

### Exemplo de uso

```python
# dados é uma lista de objetos Dados
df = montar_csv(dados)
# Cria o arquivo 'data_clean.csv'
df.to_csv("data_clean.csv", index=False)

```


# Comandos sql

```
SELECT produto_nome, SUM(quantidade) AS total_vendido
FROM produtos
WHERE data BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY produto_nome
ORDER BY total_vendido ASC;
```

## 📄 Explicação do comando SQL

O comando SQL realiza o seguinte:

- **Busca o produto baseado no nome**: `produto_nome`.  
- **Soma a quantidade vendida de cada produto**: `SUM(quantidade)` e cria um alias `total_vendido`.  
- **Origem dos dados**: `FROM produtos` indica que os dados vêm da tabela `produtos`.  
- **Filtro de datas**: `WHERE data BETWEEN '2023-06-01' AND '2023-06-30'` seleciona apenas os registros do intervalo informado.  
- **Agrupamento**: `GROUP BY produto_nome` agrupa todos os registros com o mesmo nome de produto.  
- **Ordenação**: `ORDER BY total_vendido ASC` ordena os resultados em ordem crescente; os **menos vendidos aparecem primeiro**.

✅ Este comando cumpre o objetivo de **identificar os produtos que venderam menos no mês de junho de 2024**.


## 📊 Explicação do comando SQL

O comando SQL realiza o seguinte:

- **Seleciona as colunas**: `produto_nome`, `produto_categoria` e a soma de `quantidade * produto_preco`, criando um alias `total_vendas`.  
- **Origem dos dados**: `FROM produtos` indica que os dados vêm da tabela `produtos`.  
- **Agrupamento**: `GROUP BY produto_nome, produto_categoria` soma todas as vendas do mesmo produto dentro da mesma categoria.  
- **Ordenação**: `ORDER BY total_vendas DESC` organiza os resultados em ordem decrescente, mostrando primeiro os produtos com maior faturamento.

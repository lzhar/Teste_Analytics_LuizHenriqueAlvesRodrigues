.print "Produtos que venderam menos no mês de junho de 2024"

SELECT produto_nome, SUM(quantidade) AS total_vendido
FROM produtos
WHERE data BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY produto_nome
ORDER BY total_vendido ASC;

.print "======================"

.print "Listagem de produtos por nome, categoria e a soma total de vendas. Resultado ordendado pelo valor total de vendas em ordem decrescente."

SELECT 
    produto_nome,
    produto_categoria,
    SUM(quantidade * produto_preco) AS total_vendas
FROM produtos
GROUP BY produto_nome, produto_categoria
ORDER BY total_vendas DESC;
SELECT produto_nome, SUM(quantidade) AS total_vendido
FROM produtos
WHERE data BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY produto_nome
ORDER BY total_vendido ASC;

.print "======================"

SELECT 
    produto_nome,
    produto_categoria,
    SUM(quantidade * produto_preco) AS total_vendas
FROM produtos
GROUP BY produto_nome, produto_categoria
ORDER BY total_vendas DESC;
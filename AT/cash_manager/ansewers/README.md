# Sistema de Caixa

## 15. Problema com múltiplos caixas operando ao mesmo tempo

Quando há mais de um caixa operando ao mesmo tempo no supermercado, um grande problema que pode surgir é o acesso simultâneo aos dados, como o estoque de produtos e os registros das compras. Isso pode causar o que chamamos de condição de corrida, onde o sistema não consegue gerenciar as mudanças de forma correta.
Por exemplo, se dois caixas tentarem vender a última unidade de um produto ao mesmo tempo, o sistema pode ficar confuso e acreditar que ainda há estoque disponível, quando na verdade o produto já foi vendido para o outro caixa

## 16. Solução para o problema de múltiplos caixas

Para resolver esse problema, é possível usar bloqueios (locks) para garantir que apenas um caixa tenha acesso aos dados compartilhados, como o estoque, de cada vez. Isso impede que dois caixas tentem modificar as informações ao mesmo tempo, evitando as condições de corrida.
No Python, podemos usar a biblioteca threading para implementar esses bloqueios. Cada vez que um caixa precisa acessar ou modificar os dados (por exemplo, ao adicionar um item ao carrinho ou atualizar o estoque), ele "trava" os dados, garantindo que ninguém mais possa acessá-los ao mesmo tempo. Depois que o caixa terminar, ele libera o bloqueio, permitindo que o próximo caixa possa acessar os dados.
Uma solução ainda mais robusta seria utilizar um banco de dados que já suporte o controle de concorrência de acesso simultâneo, como MySQL ou PostgreSQL, o que garantiria que o sistema lidasse melhor com o acesso simultâneo aos dados.


# Projeto: Leilão de Entregas com Visualização Gráfica

Este projeto simula um sistema de entregas com o objetivo de maximizar o lucro com base em rotas, prazos e bônus. Ele compara duas estratégias distintas de tomada de decisão:

- Versão Simples
- Versão com Inteligência Artificial (IA)

Além disso, o projeto fornece uma visualização gráfica comparativa para análise dos resultados.

---

## Como Executar

1. Instale as dependências:
   ```
   pip install matplotlib networkx pandas
   ```

2. Execute o script principal:
   ```
   python main.py
   ```

---

## Estrutura dos Arquivos

```
leilao_entregas/
│
├── dados/
│   ├── matriz_adjacencia.csv     # Tabela com tempos entre os pontos (grafo)
│   └── entregas.csv              # Lista de entregas disponíveis
│
├── modules/
│   ├── grafo.py                  # Leitura da matriz e criação do grafo
│   ├── entregas.py               # Carregamento das entregas
│   ├── versao_simples.py         # Estratégia simples de seleção
│   ├── versao_ia.py              # Estratégia IA (permutações)
│   ├── utils.py                  # Função de cálculo de rota e tempo
│   └── visualizacao.py           # Geração dos gráficos comparativos
│
└── main.py                       # Script principal
```

---

## Estratégias Utilizadas

### Versão Simples

A versão simples utiliza uma abordagem sequencial e direta:

- As entregas são avaliadas na ordem em que aparecem no arquivo.
- O algoritmo verifica se ainda é possível realizar a entrega dentro do prazo.
- Se for viável:
  - Calcula-se o tempo de ida e volta entre o ponto A (origem fixa) e o destino.
  - Se o tempo permitir, a entrega é realizada, o bônus acumulado e o entregador retorna para o ponto A.
- A próxima entrega é avaliada apenas após a finalização da anterior.

Essa estratégia é simples, eficiente e rápida para execução, mas não explora combinações mais vantajosas de entregas.

---

### Versão com IA (Força Bruta por Permutação)

A versão IA emprega uma abordagem exaustiva para identificar a melhor sequência de entregas. O algoritmo realiza os seguintes passos:

1. Gera todas as **permutações possíveis** da lista de entregas.
2. Para cada permutação:
   - Simula o processo de entrega na ordem definida.
   - Calcula o tempo total que o entregador levaria para:
     - Ir de A até o destino da entrega.
     - Retornar ao ponto A.
     - Iniciar a próxima entrega a partir de A.
   - Verifica se a entrega pode ser feita dentro do prazo.
   - Se sim, acumula o bônus e registra a entrega como realizada.
   - Caso o tempo ultrapasse o prazo, a permutação é descartada.
3. Ao final da simulação de cada permutação, verifica se:
   - O bônus total acumulado é maior que o melhor registrado até então.
   - Em caso de empate de bônus, é escolhida a sequência com **menor tempo total de execução**.
4. Retorna a melhor sequência possível com base nesses critérios.

Esta estratégia garante a solução ótima, mas tem **complexidade fatorial (O(n!))**, o que a torna inviável para grandes volumes de entregas.

---

## Visualização Gráfica

Ao final da execução, o sistema exibe uma visualização gráfica comparando as duas estratégias. São mostrados:

- O grafo com as conexões entre pontos e as rotas realmente utilizadas.
- As rotas da versão simples (em laranja) e da IA (em vermelho).
- Um gráfico de barras com:
  - Bônus total obtido por cada estratégia.
  - Tempo total (em minutos) que o entregador levou para realizar todas as entregas.

---

## Autor

Desenvolvido como parte da disciplina de Inteligência Artificial.

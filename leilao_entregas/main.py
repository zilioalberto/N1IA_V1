from modules.grafo import carregar_grafo
from modules.entregas import carregar_entregas
from modules.versao_simples import executar_versao_simples
from modules.versao_ia import executar_versao_ia
from modules.versao_heuristica import executar_versao_heuristica
from modules.visualizacao import exibir_resultados_tres_solucoes

# Carregar dados
grafo = carregar_grafo('dados/matriz_adjacencia.csv')
entregas = carregar_entregas('dados/entregas.csv')

# Executar versões
resultado_simples = executar_versao_simples(grafo, entregas)
resultado_ia = executar_versao_ia(grafo, entregas)
resultado_heuristica = executar_versao_heuristica(grafo, entregas)

# Visualizar resultados comparativos
exibir_resultados_tres_solucoes(grafo, resultado_simples, resultado_ia, resultado_heuristica)

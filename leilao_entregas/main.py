from modules.grafo import carregar_grafo
from modules.entregas import carregar_entregas
from modules.versao_simples import executar_versao_simples
from modules.versao_ia import executar_versao_ia
from modules.visualizacao import exibir_resultados_duas_solucoes

# Carregar grafo e entregas
grafo = carregar_grafo('dados/matriz_adjacencia.csv')
entregas = carregar_entregas('dados/entregas.csv')

# Executar ambas as versões
resultado_simples = executar_versao_simples(grafo, entregas)
resultado_ia = executar_versao_ia(grafo, entregas)

# Exibir comparativo completo
exibir_resultados_duas_solucoes(grafo, resultado_simples, resultado_ia)

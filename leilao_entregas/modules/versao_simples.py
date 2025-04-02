from modules.utils import calcular_tempo

def executar_versao_simples(grafo, entregas):
    tempo_atual = 0  # tempo total do entregador
    lucro_total = 0
    entregas_realizadas = []
    rotas_realizadas = []

    for inicio, destino, bonus in entregas:
        if tempo_atual <= inicio:
            ida_tempo, ida_caminho = calcular_tempo(grafo, 'A', destino)
            volta_tempo, _ = calcular_tempo(grafo, destino, 'A')

            if ida_tempo == float('inf') or volta_tempo == float('inf'):
                continue

            tempo_atual = inicio + ida_tempo + volta_tempo
            lucro_total += bonus
            entregas_realizadas.append((inicio, destino, bonus))
            rotas_realizadas.append(ida_caminho)

    return entregas_realizadas, lucro_total, rotas_realizadas, tempo_atual

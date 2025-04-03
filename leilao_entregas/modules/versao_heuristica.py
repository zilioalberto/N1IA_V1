from modules.utils import calcular_tempo

def executar_versao_heuristica(grafo, entregas):
    entregas_restantes = entregas.copy()
    tempo_atual = 0
    lucro_total = 0
    entregas_realizadas = []
    rotas_realizadas = []

    while entregas_restantes:
        melhores_opcoes = []

        for inicio, destino, bonus in entregas_restantes:
            if tempo_atual <= inicio:
                ida_tempo, ida_caminho = calcular_tempo(grafo, 'A', destino)
                volta_tempo, _ = calcular_tempo(grafo, destino, 'A')

                if ida_tempo == float('inf') or volta_tempo == float('inf'):
                    continue

                tempo_total = ida_tempo + volta_tempo
                beneficio_por_tempo = bonus / tempo_total if tempo_total > 0 else 0

                if tempo_atual + tempo_total <= 1440:  # limite de um dia
                    melhores_opcoes.append((beneficio_por_tempo, inicio, destino, bonus, tempo_total, ida_caminho))

        if not melhores_opcoes:
            break

        # Seleciona a entrega com maior benefício por tempo
        melhores_opcoes.sort(reverse=True)
        _, inicio, destino, bonus, tempo_total, caminho = melhores_opcoes[0]

        tempo_atual = max(tempo_atual, inicio) + tempo_total
        lucro_total += bonus
        entregas_realizadas.append((inicio, destino, bonus))
        rotas_realizadas.append(caminho)
        entregas_restantes.remove((inicio, destino, bonus))

    return entregas_realizadas, lucro_total, rotas_realizadas, tempo_atual

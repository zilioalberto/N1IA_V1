def calcular_tempo(grafo, origem, destino):
    visitados = set()
    fila = [(origem, 0, [origem])]  # (nó atual, tempo acumulado, caminho percorrido)

    while fila:
        atual, tempo, caminho = fila.pop(0)
        if atual == destino:
            return tempo, caminho
        visitados.add(atual)
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                fila.append((vizinho, tempo + grafo[atual][vizinho], caminho + [vizinho]))

    return float('inf'), []

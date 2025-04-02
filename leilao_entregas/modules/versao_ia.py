import itertools
from modules.utils import calcular_tempo

def executar_versao_ia(grafo, entregas):
    melhor_lucro = 0
    melhor_seq = []
    melhor_rotas = []
    menor_tempo_total = float('inf')

    for perm in itertools.permutations(entregas):
        tempo_total = 0
        lucro = 0
        realizadas = []
        rotas = []

        for inicio, destino, bonus in perm:
            if tempo_total <= inicio:
                ida, caminho_ida = calcular_tempo(grafo, 'A', destino)
                volta, _ = calcular_tempo(grafo, destino, 'A')

                if ida == float('inf') or volta == float('inf'):
                    break

                tempo_total = inicio + ida + volta
                lucro += bonus
                realizadas.append((inicio, destino, bonus))
                rotas.append(caminho_ida)
            else:
                break

        if lucro > melhor_lucro or (lucro == melhor_lucro and tempo_total < menor_tempo_total):
            melhor_lucro = lucro
            melhor_seq = realizadas
            melhor_rotas = rotas
            menor_tempo_total = tempo_total

    return melhor_seq, melhor_lucro, melhor_rotas, menor_tempo_total

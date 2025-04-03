import matplotlib.pyplot as plt
import networkx as nx

def exibir_resultados_tres_solucoes(grafo, resultado_simples, resultado_ia, resultado_heuristica):
    entregas_s, lucro_s, rotas_s, tempo_s = resultado_simples
    entregas_i, lucro_i, rotas_i, tempo_i = resultado_ia
    entregas_h, lucro_h, rotas_h, tempo_h = resultado_heuristica

    G = nx.Graph()
    for origem in grafo:
        for destino in grafo[origem]:
            G.add_edge(origem, destino, weight=grafo[origem][destino])

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(18, 10))

    # Subplot 1: Caminhos versão simples
    plt.subplot(2, 3, 1)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=1500)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edges_s = [(rota[i], rota[i+1]) for rota in rotas_s for i in range(len(rota)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_s, edge_color='orange', width=3)
    plt.title("Rotas - Simples")

    # Subplot 2: Caminhos versão IA
    plt.subplot(2, 3, 2)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=1500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edges_i = [(rota[i], rota[i+1]) for rota in rotas_i for i in range(len(rota)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_i, edge_color='red', width=3)
    plt.title("Rotas - IA")

    # Subplot 3: Caminhos versão Heurística
    plt.subplot(2, 3, 3)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=1500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edges_h = [(rota[i], rota[i+1]) for rota in rotas_h for i in range(len(rota)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_h, edge_color='green', width=3)
    plt.title("Rotas - Heurística")

    # Subplot 4: Comparação de bônus
    plt.subplot(2, 3, 4)
    plt.bar(['Simples', 'IA', 'Heurística'], [lucro_s, lucro_i, lucro_h], color=['orange', 'red', 'green'])
    plt.title("Comparação de Bônus")
    plt.ylabel("Bônus Total")

    # Subplot 5: Comparação de tempo total do entregador
    plt.subplot(2, 3, 5)
    tempos = [tempo_s, tempo_i, tempo_h]
    bars = plt.bar(['Simples', 'IA', 'Heurística'], tempos, color=['blue', 'gray', 'green'])
    plt.title("Tempo Total do Entregador")
    plt.ylabel("Tempo (min)")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f} min", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

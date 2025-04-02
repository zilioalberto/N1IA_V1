import matplotlib.pyplot as plt
import networkx as nx

def exibir_resultados_duas_solucoes(grafo, resultado_simples, resultado_ia):
    entregas_s, lucro_s, rotas_s, tempo_s = resultado_simples
    entregas_i, lucro_i, rotas_i, tempo_i = resultado_ia

    G = nx.Graph()
    for origem in grafo:
        for destino in grafo[origem]:
            G.add_edge(origem, destino, weight=grafo[origem][destino])

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(16, 8))

    # Subplot 1: Caminhos versão simples
    plt.subplot(2, 2, 1)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=1500)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edges_s = [(rota[i], rota[i+1]) for rota in rotas_s for i in range(len(rota)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_s, edge_color='orange', width=3)
    plt.title("Rotas - Versão Simples")

    # Subplot 2: Caminhos versão IA
    plt.subplot(2, 2, 2)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=1500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edges_i = [(rota[i], rota[i+1]) for rota in rotas_i for i in range(len(rota)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_i, edge_color='red', width=3)
    plt.title("Rotas - Versão IA")

    # Subplot 3: Comparação de Bônus
    plt.subplot(2, 2, 3)
    plt.bar(['Simples', 'IA'], [lucro_s, lucro_i], color=['orange', 'red'])
    plt.title("Comparação de Bônus Totais")
    plt.ylabel("Bônus Total")

    # Subplot 4: Comparação de Tempo de Entrega (minutos)
    plt.subplot(2, 2, 4)
    tempos_min = [tempo_s, tempo_i]
    bars = plt.bar(['Simples', 'IA'], tempos_min, color=['blue', 'green'])
    plt.title("Tempo Total do Entregador")
    plt.ylabel("Tempo (min)")

    # Mostrar valores nas barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f} min", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

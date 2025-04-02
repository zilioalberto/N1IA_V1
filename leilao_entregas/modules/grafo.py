import pandas as pd

def carregar_grafo(path):
    df = pd.read_csv(path, index_col=0)
    df = df.rename(columns=str.strip).rename(index=str.strip)  # Remove espaços em branco

    grafo = {}
    for origem in df.index:
        grafo[origem] = {}
        for destino in df.columns:
            tempo = df.loc[origem, destino]
            if tempo > 0:
                grafo[origem][destino] = tempo
    return grafo

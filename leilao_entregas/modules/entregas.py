import pandas as pd

def carregar_entregas(path):
    df = pd.read_csv(path)
    return list(df.itertuples(index=False, name=None))  # (inicio, destino, bonus)

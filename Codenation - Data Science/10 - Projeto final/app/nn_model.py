import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


def get_leads(port, df, k=5):
    """
        Nearest Neighbors para obter índice e distância através da similaridade

        Parâmetros
        ----------
            port = porfólio onde será obtido as ids mais próximas
            df = dataframe onde será mapeado os elementos a serem localizados
            k = número de vizinhos a serem localizados

        Default
        -------
            metric: cosine

        Return
        ------
            DataFrame
    """
    df_correct = df[df['id'].apply(lambda x: x not in port['id'].values)]
    
    nbrs = NearestNeighbors(n_neighbors= k, metric='cosine')
    
    nbrs.fit(df_correct.drop('id', axis= 1))
    
    distances, indices = nbrs.kneighbors(port.drop('id', axis= 1))
    
    distances = distances.flatten()
    indices = indices.flatten()
    
    leads = pd.DataFrame({'id': df_correct.iloc[indices]['id'].copy()})
    
    del(df_correct, distances, indices, nbrs)
    return leads

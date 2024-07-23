
import pickle
import pandas as pd
import os
def predecir_modelo(df:pd.DataFrame):
    archivo_path = 'C:/Users/rojom/Documents/proyecto/proyecto_mioti/model/modelo_texto.pkl'
    with open(archivo_path, 'rb') as file:
        loaded_pipeline = pickle.load(file)
    print(df)
    return loaded_pipeline.predict(df)
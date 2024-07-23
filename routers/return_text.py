from fastapi import APIRouter
from entitis.request_body import Request
import util.proces_text as prt 
import util.proces_pos as prs
import pandas as pd
import numpy as np
import model.use_model as md

router = APIRouter()

@router.post("/text")
def predict_text(input: Request):
    text = input.text.strip()
    df=pre_proces_text(text)
    score=md.predecir_modelo(df)
    print(type(score))
    return {"text": text,'puntuacion':score[0]}


def pre_proces_text(text):

    citas=prt.contar_citas_unico(text)
    print(citas)
    len_text=prt.longitud_texto(text)
    print(len_text)
    unic= prt.palabras_unica(text)
    print(unic)
    gramar=prt.contar_errores(text)
    print(gramar)
    embedding=prt.text_enbeding(text)
    print(type(embedding))
    # Asegurarse de que embedding es un array de Numpy
    if not isinstance(embedding, np.ndarray):
        embedding = np.array(embedding)
        # Crear un diccionario con los valores calculados
    data = {
        'unique_words': [unic],
        'citas_len': [citas],
        'longitud': [len_text],
        'Grammar_Mistakes': [gramar]
        }
    # Convertir embedding en un DataFrame y añadir prefijo a las columnas
    embedding_df = pd.DataFrame([embedding], columns=[f'embedding_{i}' for i in range(embedding.size)])
    # Crear el DataFrame final combinando el diccionario de datos y el DataFrame de embedding
    df = pd.concat([pd.DataFrame(data), embedding_df], axis=1)
    df=prs.return_df_pos(df,text)
    print('--------------------------------------------')
    print(df)
    return df 
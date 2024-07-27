import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter


nltk.download('stopwords')
stopwords = stopwords.words('english')
required_columns = ['JJ', 'NN', 'RB', 'VB', 'MD', 'otros']


def filtrar_palabras(ensayo):
    
    palabras = word_tokenize(ensayo)
    palabras_filtradas = []
    separadores = [',', '.', ';', ':', '?', '¿', '!', '¡', '...','``','','--','"',"n't",'(',')',"''"]
    
    for palabra in palabras:
        if palabra.lower() in stopwords:
            pass
        elif palabra.lower() in separadores:
            pass
        else:
            palabras_filtradas.append(palabra)
    
    return ' '.join(palabras_filtradas)


def clasificar_palabras_filtradas(palabras_filtradas):
    palabras = word_tokenize(palabras_filtradas)
    pos_tags = pos_tag(palabras)
    return pos_tags

def obtener_categoria(pos_tags):
    if pos_tags.startswith('JJ'):
        return 'JJ'
    elif pos_tags.startswith('NN'):
        return 'NN'
    elif pos_tags.startswith('RB'):
        return 'RB'
    elif pos_tags.startswith('VB'):
        return 'VB'
    elif pos_tags.startswith('MD'):
        return 'MD'
    else:
        return 'otros' 
    

def contar_categorias_pos(lista_etiquetas):
    categorias = [obtener_categoria(pos_tags) for word, pos_tags in lista_etiquetas]
    conteo = Counter(categorias)
    data = dict(conteo)
    conteo_df = pd.DataFrame([data]).drop(columns=['otros'])

    return conteo_df



def return_df_pos(df,text:str):
    text=filtrar_palabras(text)
    pos=clasificar_palabras_filtradas(text)
    cat=contar_categorias_pos(pos)
    counter_df = pd.DataFrame(cat).fillna(0).astype(int)
    df = df.join(counter_df)
    df = ensure_columns(df, required_columns)
    return df 

def ensure_columns(df, required_columns):
    # Añadir cualquier columna que falte con un valor predeterminado (0 en este caso)
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0
    return df
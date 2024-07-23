import re
from FlagEmbedding import BGEM3FlagModel
import language_tool_python

from nltk.tokenize import word_tokenize



model = BGEM3FlagModel('BAAI/bge-m3',  use_fp16=True)
tool = language_tool_python.LanguageTool('en-US')


def contar_citas_unico(text):
    # Usamos una expresión regular para encontrar las citas en el formato especificado
    citas = re.findall("\\(.*?\\)", text)
    c=0
    for i in citas:
        len_i=len(i)
        if len_i> 5 and len_i<20:
            c+=1
    return c

def longitud_texto(text):
    return len(text)

def text_enbeding(text):
    return model.encode(text)['dense_vecs']

def contar_errores(texto):
    matches = tool.check(texto)
    return len(matches)

def palabras_unica(ensayo):
    palabras=word_tokenize(ensayo)
    palabras_unicas = set(palabras)
    numero_de_palabras_unicas = len(palabras_unicas)
    return(numero_de_palabras_unicas)
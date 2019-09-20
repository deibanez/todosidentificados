from fastapi import FastAPI
import pandas as pd
from sqlalchemy import create_engine
from fuzzywuzzy import fuzz

def score(row, search,col_nom):
    """partial ratio score fuzzy"""
    sc = fuzz.partial_ratio(row[col_nom].lower(), search.lower())
    return sc

def select_first_name(serie_lista_row, keep='first_alpha', min_len=5, max_names 
= 4):
    for i in serie_lista_row:
        if keep == 'first_alpha':
            str_j =  ''.join(filter(str.isalpha, i))
            if len(str_j) >=  min_len:
                if len(i.split(' ')) <= max_names:
                    return i
                else:
                    return '-'
            else:
                return '-'

def buscar_n_fichas(search, df_, col_nom='nombre', col_id='fichias_id', n_=10, cols=['nombre', 'fichas_id']):
    scores = df.apply(score, search=str(search).lower(), col_nom=col_nom, axis=1)
    df['score'] = scores
    print(n_)
    df_r  = df.sort_values(by='score', ascending=False).iloc[:n_][cols]
    return df_r


#app.config.from_object('config')
#psql = app.config["PSQL"]
psql = {'host':'users-db','port':'5432','db':'fichas_dina', 'user':'postgres','pass':'postgres'}
engine= create_engine('postgresql://{}:{}@{}:{}/{}'.format(psql['user'],psql['pass'],psql['host'],psql['port'],psql['db']))

df = pd.read_sql('fichas', con=engine)

print('##Datos cargados\nN fichas:{}'.format(len(df)))

serie_lista = df.ficha_str.str.split('\n')
nombre_de_ficha = serie_lista.apply(select_first_name, min_len=10,max_names = 7)
df['nombre'] = nombre_de_ficha.tolist()

print('## nombres_seleccionados')


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/buscador_fichas/{query}")
def buscador_fichas(query: str):
    print('holaaa')
    #print(query, n)
    df_ = buscar_n_fichas(search=query, n_=10, df_=df)
    return df_.to_json(orient='index')

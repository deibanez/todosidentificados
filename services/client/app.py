from flask import render_template
from flask import Flask, session, redirect, url_for, escape, request
import pandas as pd
import requests
import urllib.parse

app = Flask(__name__, instance_relative_config=True)


def alistar_links_df(row):
    return "<a href={} target='_blank'>{} {}</a>".format(url_for('static',filename='images/'+row['fichas_id']+".jpg"),row['nombre'],row['score'])

@app.route('/', methods= ['POST','GET'])
def index():
    if request.method == 'POST':
        busqueda = request.form["busqueda"]
        query = urllib.parse.quote(busqueda)
        req = requests.get('http://users:80/buscador_fichas/'+query)
        resp = req.json()
        df_ = pd.read_json(resp, orient='index')
        df_ = df_.sort_values(by='score', ascending=False)
        df_f = pd.DataFrame({'Resultados de búsqueda: ': df_.apply(alistar_links_df, axis=1).tolist()})
        return render_template('buscador.html',resultado=[df_f.to_html(header="true",index=False, escape=False)])
    return render_template('buscador.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

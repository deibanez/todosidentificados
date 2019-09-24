from flask import render_template
from flask import Flask, session, redirect, url_for, escape, request
import pandas as pd
import requests
import urllib.parse
import json

app = Flask(__name__, instance_relative_config=True)


def alistar_links_df(row):
    return "<a href={} target='_blank'>{}</a>".format(url_for('static',filename='images_250ppi/'+row['id']+".jpg"),row['nombre'])#,row['score'])

@app.route('/', methods= ['POST','GET'])
def fichas():
    if request.method == 'POST':
        busqueda = request.form["busqueda"]
        query = urllib.parse.quote(busqueda)
        req = requests.get('http://users:80/buscador_fichas/'+query)
        resp = json.loads(req.json())
        df = pd.DataFrame()
        for i, k in resp.items():
            id_ = i
            nom = list(k.keys())[0]
            score = list(k.values())[0]

            df = df.append(pd.DataFrame({'id': [id_], 'nombre': [nom], 'score': [score]}), ignore_index=True)

        df = df.sort_values(by='score', ascending=False)
        df_f = pd.DataFrame({'Resultados de búsqueda: ': df.apply(alistar_links_df, axis=1).tolist()})
        return render_template('buscador.html',resultado=[df_f.to_html(header="true",index=False, escape=False)])
    return render_template('buscador.html', fichas=True)

@app.route("/who", methods=['GET'])
def who():
    return render_template('buscador.html', who=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

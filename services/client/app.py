from flask import render_template
from flask import Flask, session, redirect, url_for, escape, request
import pandas as pd

def alistar_links_df(row):
    return "<a href={} target='_blank'>{}</a>".format(url_for('static',filename='images/'+row['fichas_id']+".jpg"),row['nombre'])

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
psql = app.config["PSQL"]

@app.route('/', methods= ['POST','GET'])
def index():
    if request.method == 'POST':
        busqueda = request.form["busqueda"]

        df_ = request.get('http://users:5432/buscador_fichas/'+busqueda)
        
        df_f = pd.DataFrame({'Resultados de búsqueda: ': df_.apply(alistar_links_df, axis=1).tolist()})
        return render_template('buscador.html',resultado=[df_f.to_html(header="true",index=False, escape=False)])
    return render_template('buscador.html')

if __name__ == '__main__':
    app.run(hostdebug=True)

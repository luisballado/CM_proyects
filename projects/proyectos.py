from flask import Flask, render_template, request, url_for, flash, redirect
from flask import jsonify
import json

from set_theory import *

app = Flask(__name__)

# Menu Inicio
@app.route('/')
def index():
    return render_template('index.html')

#Pag relacionada al proyecto uno
@app.route('/project_one', methods=['GET', 'POST'])
def project_one():

    resultados = []

    resultado = request.args.to_dict()
        
    if resultado:
        r = resultado['resultados']
        r_json = r.replace("'", "\"")

        print(r_json)
        
        d = json.loads(r_json)
        
        resultados.append(d)
                
    if request.method == 'POST':

        respuesta = {}
        
        set_A = request.form['conjunto1']
        set_B = request.form['conjunto2']

        st = SetTheory(set_A,set_B)

        respuesta['display'] =  st.display()
        respuesta['cardinality'] = st.cardinality()
                
        respuesta['comparision'] = str(st.comparision()['equals'])

        respuesta['difference'] = st.difference()
        respuesta['union'] = st.union()
        respuesta['intersection'] = st.intersection()
        
        return redirect(url_for('project_one',resultados=respuesta))
    
    return render_template('project_one.html',resultados=resultados)

#Pag relacionada al proyecto dos
@app.route('/project_two', methods=['GET','POST'])
def project_two():
    resultados = []
    
    return render_template('project_two.html', resultados = resultados)

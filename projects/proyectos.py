from flask import Flask, render_template, request, url_for, redirect
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

        json_formatted = json.dumps(d, indent=3)
        print(json_formatted)
        
        resultados.append(d)
                
    if request.method == 'POST':

        set_A = request.form['conjunto1']
        set_B = request.form['conjunto2']
        
        respuesta = {}
        respuesta_arr = []
        
        st = SetTheory(set_A,set_B)

        #--- hacer respuesta ---
        tmp = {}
        tmp['type_op'] = 'display'
        tmp['A'] = st.display()['A']
        tmp['B'] = st.display()['B']
        respuesta_arr.append(tmp)
        
        tmp = {}
        tmp['type_op'] = 'cardinality'
        tmp['operation'] = st.cardinality()
        respuesta_arr.append(tmp)

        tmp = {}
        tmp['type_op'] = 'power_set'
        tmp['operation'] = {'A':st.power_set(st.A),'B':st.power_set(st.B)}
        respuesta_arr.append(tmp)

        tmp = {}
        tmp['type_op'] = 'all_posible_partitions'
        tmp['operation'] = {'A':'{}','B':'{}'}
        respuesta_arr.append(tmp)

        respuesta['unary_op'] = respuesta_arr 

        respuesta_arr = []
        
        tmp = {}
        tmp['type_op'] = 'comparision'
        tmp['operation'] = str(st.comparision()['equals'])
        respuesta_arr.append(tmp)
        
        tmp = {}
        tmp['type_op'] = 'subset'
        tmp['operation'] = {'AB':'{}','BA':'{}'}
        respuesta_arr.append(tmp)

        tmp = {}
        tmp['type_op'] = 'proper_subset'
        tmp['operation'] = {'AB':'{}','BA':'{}'}
        respuesta_arr.append(tmp)

        tmp = {}
        tmp['type_op'] = 'difference'
        tmp['operation'] = st.difference()
        respuesta_arr.append(tmp)
        
        tmp = {}
        tmp['type_op'] = 'symmetric_diff'
        tmp['operation'] = {'AB':'{}','BA':'{}'}
        respuesta_arr.append(tmp)

        tmp = {}
        tmp['type_op'] = 'union'
        tmp['operation'] = st.union()
        respuesta_arr.append(tmp)
        
        tmp = {}
        tmp['type_op'] = 'intersection'
        tmp['operation'] = str(st.intersection()['Intersection'])
        tmp['disjoint'] = str(st.intersection()['disjoint'])
        respuesta_arr.append(tmp)
        
        tmp = {}
        tmp['type_op'] = 'cartesian_product'
        tmp['operation'] = {'AB':'{}','BA':'{}'}
        respuesta_arr.append(tmp)
        
        respuesta['binary_op'] = respuesta_arr 
                
        print(respuesta)
        
        #redirect(url_for('project_one',resultados=respuesta))
        return jsonify(respuesta) 
    
    return render_template('project_one.html',resultados=resultados)

#Pag relacionada al proyecto dos
@app.route('/project_two', methods=['GET','POST'])
def project_two():
    resultados = []
    
    return render_template('project_two.html', resultados = resultados)

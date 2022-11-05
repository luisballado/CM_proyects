from flask import Flask, render_template, request, url_for, redirect
from flask import jsonify
import json

from set_theory import *
from relations_and_functions import *

app = Flask(__name__)

# Menu Inicio
@app.route('/')
def index():
    return render_template('index.html')

#Hacer todos los calculos en nueva ruta
@app.route('/calc_sets', methods=['POST'])
def calc_sets():

    #obtener valores ingresados
    set_A = request.json['conjunto1']
    set_B = request.json['conjunto2']
    
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
    tmp['operation'] = {'AB':st.subset(True),'BA':st.subset(False)}
    respuesta_arr.append(tmp)
    
    tmp = {}
    tmp['type_op'] = 'proper_subset'
    tmp['operation'] = {'AB':st.proper_subset(True),'BA':st.proper_subset(False)}
    respuesta_arr.append(tmp)
    
    tmp = {}
    tmp['type_op'] = 'difference'
    tmp['operation'] = {'AB':str(st.difference()),'BA':str(st.difference(False))}
    respuesta_arr.append(tmp)
    
    tmp = {}
    tmp['type_op'] = 'symmetric_diff'
    tmp['operation'] = {'AB':str(st.symmetric_diff(True)),'BA':str(st.symmetric_diff(False))}
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
    tmp['operation'] = {'AB':str(st.cartesian_product(True)),'BA':str(st.cartesian_product(False))}
    respuesta_arr.append(tmp)
    
    respuesta['binary_op'] = respuesta_arr 
    
    #print(respuesta)
    
    return jsonify(respuesta)
    
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
        
        return redirect(url_for('project_one',resultados=respuesta))
        #return jsonify(respuesta) 
    
    return render_template('project_one.html',resultados=resultados)

#Hacer todos los calculos de funciones en nueva ruta
@app.route('/calc_functions', methods=['POST'])
def calc_functions():

    #obtener valores ingresados
    a = request.json['conjunto1']
    b = request.json['conjunto2']
    calculation = request.json['calculation']
    
    if calculation == 'relations':

        st = SetTheory(a,b)

        #producto cartesiano
        PC = []
        for i in st.A:
            for j in st.B:
                t2 = []
                t2.append(str(i))
                t2.append(str(j))
                PC.append(t2)
                
        relaciones = st.power_set(PC)
        
        resultados = []
        
        calc_functions_and_relations = True
        respuesta_arr = []

        for r in relaciones:
            #print('###############')
            tmp = {}
            rf = RFunctions(r)
            print(rf.rf)
            tmp['relation'] = rf.style()
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
            
        return jsonify(respuesta_arr)
    
    elif calculation == 'functions':

        st = SetTheory(a,b)

        #producto cartesiano
        PC = []
        for i in st.A:
            for j in st.B:
                t2 = []
                t2.append(str(i))
                t2.append(str(j))
                PC.append(t2)
                
        relaciones = st.power_set(PC)
        
        resultados = []
        
        calc_functions_and_relations = True
        respuesta_arr = []
        
        for r in relaciones:
            #print('###############')
            tmp = {}
            rf = RFunctions(r)
            #if rf.isFunction():
            tmp['relation'] = rf.style()
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
                
        return jsonify(respuesta_arr)

    elif calculation == 'inyective':
        st = SetTheory(a,b)

        #producto cartesiano
        PC = []
        for i in st.A:
            for j in st.B:
                t2 = []
                t2.append(str(i))
                t2.append(str(j))
                PC.append(t2)
                
        relaciones = st.power_set(PC)
        
        resultados = []
        
        calc_functions_and_relations = True
        respuesta_arr = []
        
        for r in relaciones:
            #print('###############')
            tmp = {}
            rf = RFunctions(r)
            #if rf.isFunction() and rf.isInyective():
            tmp['relation'] = rf.style()
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
                
        return jsonify(respuesta_arr)

    elif calculation == 'sobreyective':
        st = SetTheory(a,b)

        #producto cartesiano
        PC = []
        for i in st.A:
            for j in st.B:
                t2 = []
                t2.append(str(i))
                t2.append(str(j))
                PC.append(t2)
                
        relaciones = st.power_set(PC)
        
        resultados = []
        
        calc_functions_and_relations = True
        respuesta_arr = []
        
        for r in relaciones:
            #print('###############')
            tmp = {}
            rf = RFunctions(r)
            #if rf.isFunction() and rf.isSobreyective():
            tmp['relation'] = rf.style()
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
                
        return jsonify(respuesta_arr)

    elif calculation == 'biyective':
        st = SetTheory(a,b)

        #producto cartesiano
        PC = []
        for i in st.A:
            for j in st.B:
                t2 = []
                t2.append(str(i))
                t2.append(str(j))
                PC.append(t2)
                
        relaciones = st.power_set(PC)
        
        resultados = []
        
        calc_functions_and_relations = True
        respuesta_arr = []
        
        for r in relaciones:
            #print('###############')
            tmp = {}
            rf = RFunctions(r)
            #if rf.isFunction() and rf.isBiyective():
            tmp['relation'] = rf.style()
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
            
        return jsonify(respuesta_arr)

    elif calculation == 'especial':

        #Validar que el conjunto especial forme parte del Dominio y Co-dominio
        special = request.json['conjuntoe']
        
        arr1 = ''
        arr2 = ''
        c = 0

        _A_ = a
        _B_ = b
        
        print(special)

        for char in range(len(special)):
            if special[c] == '(':
                arr1 = arr1 + special[c+1] + " "
                arr2 = arr2 + special[c+3] + " "
            c = c + 1

        #sys.exit()
        a = arr1.replace(" ", "")
        b = arr2.replace(" ", "")

        #construir PC
        arr_x = []
        for _a_,_b_ in zip(a,b):
            arr_tmp = []
            arr_tmp.append(_a_)
            arr_tmp.append(_b_)
            
            #TODO: RECONOCER LOS CARACTERES NO SOLAMENTE SI ESTA O NO
            if _a_ not in _A_:
                #romper y regresar error de que este elemento no se encuentra en el dominio
                return ('EN RELACIONES ESPECIFICAS ' + '"'+ _a_ +'"'
                        + " DEBE ESTAR EN EL DOMINIO"+" {"+_A_+"}"), 500
            if _b_ not in _B_:
                #romper y regresar error de que este elemento no se encuentra en el codominio
                return ('EN RELACIONES ESPECIFICAS ' + '"'+ _b_ +'"'
                        + " DEBE ESTAR EN EL CO-DOMINIO"+" {"+_B_+"}"), 500
            
            arr_x.append(arr_tmp)

        #print(arr_x)
        respuesta_arr = []

        for r in [arr_x]:
            print('###############')
            tmp = {}
            rf = RFunctions(r)
            print("RF")
            print(rf.rf)
            
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            tmp['relation'] = rf.style()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
            
            #print(rf.rf)
                    
        return jsonify(respuesta_arr)

#Pag relacionada al proyecto dos
@app.route('/project_two', methods=['GET','POST'])
def project_two():
    resultados = []
    
    return render_template('project_two.html', data = resultados)

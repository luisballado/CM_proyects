from relations_and_functions import *
from set_theory import *
import json
import sys

a = "1 2"
b = "a b"

_special_ = False


if _special_:

    ############### START SPECIAL #####################
    ####  No hacer power set ni producto cartesiano
    ###################################################

    special = '(1,a),(2,b),(2,s),(3,f)'
    arr1 = ''
    arr2 = ''
    c = 0

    print(special)

    for char in range(len(special)):
        if special[c] == '(':
            arr1 = arr1 + special[c+1] + " "
            arr2 = arr2 + special[c+3] + " "
        c = c + 1

    print(arr1)
    print(arr2)

    #sys.exit()
    a = arr1.replace(" ", "")
    b = arr2.replace(" ", "")
    
    #construir PC
    arr_x = []
    for _a_,_b_ in zip(a,b):
        arr_tmp = []
        arr_tmp.append(_a_)
        arr_tmp.append(_b_)
        arr_x.append(arr_tmp)

    respuesta_arr = []

    for r in [arr_x]:
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
    
        #print(rf.rf)
    print(json.dumps(respuesta_arr,indent=4))

    sys.exit()

################## END SPECIAL #####################
    
    
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

calc_functions_and_relations = False
respuesta_arr = []

#hacer en un for para cada elemento
if calc_functions_and_relations:
    for r in relaciones:
        #print('###############')
        tmp = {}
        rf = RFunctions(r)
        #print(rf.rf)
        tmp['relation'] = rf.style()
        tmp['is_relation'] = rf.isRelation()
        tmp['is_function'] = rf.isFunction()
        tmp['is_inyective'] = rf.isInyective()
        tmp['is_suprayective'] = rf.isSobreyective()
        tmp['is_biyective'] = rf.isBiyective()
        #tmp['specific_relation'] = rf.specific_relation()
        respuesta_arr.append(tmp)
        
        #print(rf.rf)
else:
    print("Calc Functions")
    for r in relaciones:
        #print('###############')
        tmp = {}
        rf = RFunctions(r)
        if rf.isFunction():
            tmp['relation'] = rf.style()
            tmp['is_relation'] = rf.isRelation()
            tmp['is_function'] = rf.isFunction()
            tmp['is_inyective'] = rf.isInyective()
            tmp['is_suprayective'] = rf.isSobreyective()
            tmp['is_biyective'] = rf.isBiyective()
            #tmp['specific_relation'] = rf.specific_relation()
            respuesta_arr.append(tmp)
    
#print(json.dumps(respuesta_arr,indent=4))

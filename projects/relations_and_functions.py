'''
Clase para manejar funciones y relaciones
@autor: Luis Ballado
'''

class RFunctions():

    def __init__(self,rf):

        self.rf = rf

    def style(self):
        """
        regresar con estilo
        """
        resp = []
        for _r_ in self.rf:
            t_r = list()
            for r1 in _r_:
                t_r.append(r1)
            resp.append(tuple(t_r))
        resp = str(resp)
        
        return resp.replace('[','{').replace(']','}')
        
        
    def isFunction(self):
        '''
        Determinar si es una funcion
        Una funcion es una relacion en donde a cada elemento de un conjunto A le corresponde uno
        y solo un elemento de otro conjunto B
        '''
        if len(self.rf) == 0:
            return False
        elif len(self.rf) == 1:
            return True
        else:
            resp = False
            dom_temp = ''
            for _r_ in self.rf:
                if dom_temp != _r_[0]:
                    resp = True
                else:
                    resp = False
                    break
                dom_temp = _r_[0]
            
            return resp

    def isRelation(self):
        '''
        Determinar si es una relacion
        A relation in math is a set of ordered pairs
        defining the relation between two sets.
        A relation may or may not be a function
        Example: {(1,x),(1,y),(4,z)}
        '''

        if len(self.rf) == 0:
            return True
        else:
            return True

    def calc_relations(self):
        '''
        Calcular todas las posibles relaciones
        regresar todas las relaciones posibles
        Se regresa todo
        '''
        
        return False

    def calc_functions(self):
        '''
        Calcular todas las posibles funciones
        regresar todas las funciones posibles
        Se regresa solo las que sean funciones
        '''

        
        for r in self.rf:
            if self.isFunction():
                print("funcion")
                
        
        return False

    
    def isInyective(self):
        '''
        Calcular Funciones Inyectivas
        One to one function
        Cada elemento del conjunto de llegada corresponde como maximo
        a un elemento del conjunto de partida.
        le llega una o ninguna 
        ejemplo:
        partida llegada
        1     -->  a   
        2     -->  b
        3     -->  c
        4
        NO IMPORTA QUE SOBREN
        '''
        
        if (self.isFunction()):
            
            if len(self.rf) == 1:
                return True
            else:
                #verificar que no se repita el segundo elemento
                resp = False
                dom_temp = ''
                for _r_ in self.rf:
                    if dom_temp != _r_[1]:
                        resp = True
                    else:
                        resp = False
                        break
                    dom_temp = _r_[1]
            
                return resp
        else:
            return False
        
        
    def isSobreyective(self):
        '''
        Calcular Funciones Sobreyectivas
        Onto function If all the elements of B are images of some elements of A
        Cada elemento del conjunto de llegada le corresponde por lo menos un elemento
        del conjunto de partida
        NO SOBRA
        
        ejemplo:
        partida llegada
        1     -->  a   
        2     -->  b
        3     -->  c
        4     -->  d
        5     -->  d
        
        1     -->  a   
        2     -->  a
        3     -->  a
        4     -->  a
        5     -->  a

        '''

        if (self.isFunction()):
            
            if len(self.rf) == 1:
                return True
            else:
                #verificar que no se repita el segundo elemento
                resp = False
                dom_temp = ''
                for _r_ in self.rf:
                    if dom_temp != _r_[1]:
                        resp = True
                    else:
                        resp = True
                        break
                    dom_temp = _r_[1]
            
                return resp
        else:
            return False
        
    def isBiyective(self):
        '''
        Calcular Funciones Biyectivas
        Bijective function that is both one to one and onto at the same time
        Comple las dos condiciones son Inyectivas y sobreyectivas
        
        Inyectiva
        Sobreyectiva
        Biyectiva
        1 --> a
        2 --> b
        3 --> c
        4 --> c
        '''
        
        if self.isInyective() and self.isSobreyective():
            return True
        else:
            return False
        
    def specific_relation(self,conj_esp=None):
        '''
        Calcular Relaciones Especificas
        (a,b)
        '''
        # La aplicacion interpretara que a es un elemento de A
        # y b es un elemento de B
        
        return False

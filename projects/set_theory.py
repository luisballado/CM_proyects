'''
Clase para manejar las operaciones de teoria de conjuntos
@autor: Luis Ballado
'''

def _cardinality_(X):
    count_X = 0
    for i in X:
        count_X = count_X + 1

    return count_X

class SetTheory():

    def __init__(self,A=None,B=None):
       self.__author__ = "Luis Ballado"
       self.__version__ = "1.0"
       self.A = A
       self.B = B

    #Regresar objeto de la lista recibida al iniciar
    def display(self):

        result = {}

        if self.B is not None:
            result['A'] = self.A
            result['B'] = self.B
        else:
            result['A'] = self.A 
            
        return result

    def cardinality(self):
        #The cardinality of a set is its size.
        #For a finite set, the cardinality of a set is the number of members it contains
        # Intentar no usar len()

        result = {}
        
        if self.A is not None:
            count_A = 0
            for i in self.A:
                count_A = count_A + 1
            result['A'] = count_A
            
        if self.B is not None:
            count_B = 0
            for i in self.B:
                count_B = count_B + 1
            result['B'] = count_B    
                
        return result
    
    def power_set():
        return None

    def possible_partitions():
        return None

    def comparision(self):
        '''
        comparasion de dos conjuntos
        todos los elementos en A deben estar en B y viceversa
        We say two sets are equal if they have exactly the same members
        '''

        #try one
        #hacer un recorrido con cada elemento de A que aparezca en B
        #comparar la cardinanlidad de ambos para definir que son iguales

        size_A = _cardinality_(self.A)
        size_B = _cardinality_(self.B)

        if size_A != size_B:
            return {'equals':False}

        for i in self.A:
            for j in self.B:
                if self.A[i+j] == self.B[j]:
                    print('equals')
                    break
                else:
                    print('not equals')
        
        return None

    def subset():
        return None

    def proper_subset():
        return None

    def difference():
        return None

    def symmetric_diff():
        return None

    def union():
        #The union of two sets A and B is the collection of all objects that are in either set. It is written A U T
        #Example S = {1,2,3}, T = {1,3,5} S U T = {1,2,3,5}
        
        return None

    def intersection():
        #The intersection of two sets S and T is the collection of all objects that are in both sets.
        #if A and B are sets and A (intersection) B = Vacio then we say that A and B are disjoint, or disjoint sets.
        return None

    def cartesian_product():
        return None
       
       

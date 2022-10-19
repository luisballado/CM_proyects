'''
Clase para manejar las operaciones de teoria de conjuntos
@autor: Luis Ballado
'''

import re
import math

#estilo bonito conjunto
def set_style(_set_):

    R = '{'
    
    for index, a in enumerate(_set_):
        if index != len(_set_)-1:
            R+= a+','
        else:
            R+= a
            
    R+='}'
    
    return R


class SetTheory():

    ## UNARY OPERATIONS ##
    def __init__(self,A=None,B=None):
        self.A = A
        self.B = B
        
        #Convertir de un string a lista
        if (A is not None and (type(A) == str or type(A) == int or type(A) == float)):
            
            split_sentence = []
            tmp = ''

            for s in self.A:
                if bool(re.search(r',\s+|,|-|_|;|\s+,|\s',s)):
                    if tmp != '':
                        split_sentence.append(tmp.upper())
                        tmp = ''
                else:
                    tmp += s
                    
            if tmp:
                split_sentence.append(tmp.upper())

            self.A = split_sentence

        if (B is not None and (type(B) == str or type(B) == int or type(B) == float)):
        
            split_sentence = []
            tmp = ''

            for s in self.B:

                if bool(re.search(r',\s+|,|-|_|;|\s+,|\s',s)):
                    if tmp != '':
                        split_sentence.append(tmp.upper())
                        tmp = ''
                else:
                    tmp += s
                    
            if tmp:
                split_sentence.append(tmp.upper())

            self.B = split_sentence
            
    #Regresar objeto de la lista recibida al iniciar
    def display(self):
        
        result = {}

        AA = set_style(self.A)
        result['A'] = AA
        
        if self.B is not None:
                        
            BB = set_style(self.B)
            result['B'] = BB
            
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


    def power_set(self,C):
        '''
        Es el set que contiene todos los subsets de un set y tendra los elementos de 2^|cardinalidad del set|
        '''
        A = []
        if len(C) == 0:
            return [[]]
        else:
            smaller_set = self.power_set(C[:-1])
            last_item = C[-1]
            subsets = []
            
            for item in smaller_set:
                subsets.append(item + [last_item])
                A.append(set_style(item+[last_item]))
                print(A)

            result = smaller_set + subsets
            
            return result
        
    def possible_partitions(self):
        '''
        '''
        return None

    ## Binary Operations ##
    def comparision(self):
        '''
        comparasion de dos conjuntos
        todos los elementos en A deben estar en B y viceversa
        We say two sets are equal if they have exactly the same members
        '''

        #try one
        #hacer un recorrido con cada elemento de A que aparezca en B
        #comparar la cardinanlidad de ambos para definir que son iguales

        size_A = len(self.A)
        size_B = len(self.B)
                
        if size_A != size_B:
            return {'equals':False}

        equals_A = False
        for x in self.A:
            if x in self.B:
                equals_A = True

            if not equals_A:
                break

        equals_B = False
        for x in self.B:
            if x in self.A:
                equals_B = True

            if not equals_B:
                break

        if equals_A and equals_B:
            return {'equals':True}
        else:
            return {'equals':False}

    def intersection(self):
        '''
        The intersection of two sets S and T is the collection of all objects that are in both sets.
        if A and B are sets and A (intersection) B = Vacio then we say that A and B are disjoint, or disjoint sets.
        '''
        result={}
        value = []
        for x in self.A:
            if x in self.B:
                value.append(x)

        result['Intersection'] = set_style(value)

        if not value:
            result['disjoint'] = True
        else:
            result['disjoint'] = False
            
        return result
        
    def difference(self,AxB=True):
        '''
        Is the set of all elements that are in A and not B
        Two sets are called disjoint if, and only if, they have no elements in common.
        '''
        result = []
        
        if AxB:
            for a in self.A:
                if a not in self.B:
                    result.append(a)
        else:
            for b in self.B:
                if b not in self.A:
                    result.append(b)

        
        return set_style(result)

    def union(self):
        '''
        The union of two sets A and B is the collection of all objects that are in either set. It is written A U T
        Example S = {1,2,3}, T = {1,3,5} S U T = {1,2,3,5}
        '''
        result = []

        for a in self.A:
            if a in self.B:
                result.append(a)
            else:
                result.append(a)

        for b in self.B:
            if b not in result:
                result.append(b)
                        
        return set_style(result)

    
    def cartesian_product(self):
        '''
        
        '''
        return None
       

    

    def subset(self):
        '''
        Check whether one set is a subset of other.
        Order the elements of both sets and successively compare each elemnt of the first set
        with each element of the second set.
        If some element of the first set is not found to equal any element of the second, then
        the first set is not a subset of the second.
        But if each element of the first set is found to equal an element of the second set, then
        the first set is a subset of the second.
        '''
                
        return None

    def proper_subset(self):
        """
        If C,D are sets from a universe U, we say thar C is a subset of D and write C (subset) D, or D (subset) C, if every element of C is an element of D. If in addition, D contains an element that is not in C, then C is called a proper subset of D, and
        """
        return None
    
    def symmetric_diff(self):
        '''
        '''
        return None

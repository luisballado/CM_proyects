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
        if (A is not None and (type(A) == str or type(A) == int)):
            
            split_sentence = []
            tmp = ''

            for s in self.A:
                if bool(re.search(r'\.|,\s+|,|-|_|;|\s+,|\s',s)):
                    if tmp != '':
                        #omitir si ya se encuentra en la lista
                        if tmp not in split_sentence:
                            split_sentence.append(tmp)
                        tmp = ''
                else:
                    tmp += s.upper()
                    
            if tmp:
                #omitir si ya se encuentra en la lista
                if tmp not in split_sentence:
                    split_sentence.append(tmp)

            self.A = split_sentence
            
        if (B is not None and (type(B) == str or type(B) == int)):
        
            split_sentence = []
            tmp = ''

            for s in self.B:
                if bool(re.search(r'\.|,\s+|,|-|_|;|\s+,|\s',s)):
                    if tmp != '':
                        #omitir si ya se encuentra en la lista
                        if tmp not in split_sentence:
                            split_sentence.append(tmp)
                        tmp = ''
                else:
                    tmp += s.upper()
                    
            if tmp:
                #omitir si ya se encuentra en la lista
                if tmp not in split_sentence:
                    split_sentence.append(tmp)

            self.B = split_sentence
            
    #Regresar objeto de la lista recibida al iniciar
    def display(self):
        
        result = {}
        
        AA = set_style(self.A)
        #AA = set(self.A)
        result['A'] = str(AA)
        
        if self.B is not None:
                        
            BB = set_style(self.B)
            #BB = str(set(self.B))
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
        Es el set que contiene todos los subsets de un set
        y tendra los elementos de 2^|cardinalidad del set|
        '''
        A = []
        if len(C) == 0:
            return [[]]
        else:
            peque_set = self.power_set(C[:-1]) #quitarle el ultimo a la lista
            ult_item = C[-1] #obtener el ultimo elemento de la lista
            subsets = []
            
            for item in peque_set:
                subsets.append(item + [ult_item])
                #A.append(set_style(item+[ult_item]))
                
            result = peque_set + subsets
            
            return result
        
    def possible_partitions(self, current=[],final=[]):
        '''
        Posibles particiones de un conjunto
        '''

        #caso base
        if len(lst) == 0:
            if len(current) == 0:
                print (final)
            elif len(current) > 1:
                print ([current] + final)
        else:
            part(lst[1:], current + [lst[0]], final[:])
            part(lst[1:], current[:], final + [[lst[0]]])
        
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
                result = []

        for b in self.B:
            if b not in result:
                result.append(b)
                                
        return set_style(result)

    
    def cartesian_product(self,AxB=True):
        '''
        Producto cartesiano de dos arreglos
        '''
        
        PC = []
        if(AxB):
            for i in self.A:
                t1 = []
                for j in self.B:
                    t2 = []
                    t2.append(str(i))
                    t2.append(str(j))
                    t1.append((t2))
                PC.append((t1))
        else:
            for i in self.B:
                t1 = []
                for j in self.A:
                    t2 = []
                    t2.append(str(i))
                    t2.append(str(j))
                    t1.append((t2))
                PC.append((t1))
        '''
        PC = []
        for i in self.A:
            for j in self.B:
                PC.append((i,j))
        
        return PC
        '''
        return PC
    

    def subset(self,AB=True):
        '''
        Check whether one set is a subset of other.
        '''
        isSubset = True

        if AB:
            for a in self.A:
                if a not in self.B:
                    isSubset = False

            if isSubset == False:
                return "A no es subset de B"
            else:
                return "A es subset de B"
        else:
            for b in self.B:
                if b not in self.A:
                    isSubset = False

            if isSubset == False:
                return "B no es subset de A"
            else:
                return "B es subset de A"
            
        return None

    def proper_subset(self,AB=True):
        """
        A is a proper subset of B iff there is at
        least one element in B that is not in A
        @No terminado
        """

        isPSubset = True

        if AB:
            for a in self.A:
                if a not in self.B:
                    isPSubset = False
                else:
                    isPSubset = True
                    
            if isPSubset == False:
                return "A no es proper subset de B"
            else:
                if(len(self.A)==len(self.B)):
                    return "A no es proper subset de B"
                else:
                    return "A es proper subset de B"
        else:
            for b in self.B:
                if b not in self.A:
                    isPSubset = False

            if isPSubset == False:
                return "B no es proper subset de A"
            else:
                if(len(self.B)==len(self.A)):
                    return "B no es proper subset de A"
                else:
                    return "B es proper subset de A"
                
        return None
    
    def symmetric_diff(self,AminB=True):
        '''
        returns all the items present in given sets, except the items in their intersections
        '''

        result = []
        if AminB:
            for a in self.A:
                if a in self.B:
                    result = []
                else:
                    result.append(a)

            for b in self.B:
                if b not in self.A:
                    result.append(b)
        else:
            for b in self.B:
                if b in self.A:
                    result = []
                else:
                    result.append(b)

            for a in self.A:
                if a not in self.B:
                    result.append(a)
        
        return set_style(result)

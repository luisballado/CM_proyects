
#validar si los elementos son iguales
def comparision(A,B):
    iguales = False

    if len(A) != len(B):
        return iguales
    
    for i in range(len(A)):
        if A[i] == B[i]:
            iguales = True
        else:
            iguales = False
            break

    return iguales
            
def cardinalidad(X):
    
    cardinalidad = 0

    for _a_ in X:
        cardinalidad = cardinalidad + 1

    return cardinalidad

def display(X):

    print(X)

    return None
        

    


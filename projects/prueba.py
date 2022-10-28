from set_theory import *

A = "2,3"
B = "5,6,7"

st = SetTheory(A,B)

print('###DISPLAY###')
print(st.display())

# Prints partitions of a set : [1,2] -> [[1],[2]], [[1,2]] 
def part(lst, current=[], final=[]):
    res = []
    if len(lst) == 0:
        if len(current) == 0:
            print('final')
            print (final)
        elif len(current) > 1:
            print('current plus final')
            print ([current] + final)
    else:
        part(lst[1:], current + [lst[0]], final[:])
        part(lst[1:], current[:], final + [[lst[0]]])
    
'''
print('###CARDINALITY###')
print(st.cardinality())
print('###COMPARISION###')
print(st.comparision())
print('###INTERSECTION###')
print(st.intersection())
print('###DIFFERENCE A-B###')
print(st.difference())
print('###DIFFERENCE B-A###')
print(st.difference(False))
print('###UNION###')
print(st.union())
'''
A = st.A
B = st.B

#print('###POWER SET A###')
#print(st.power_set(A))
#print('###POWER SET B###')
#print(st.power_set(B))
#print(part(['math','is','fun']))

c_p = ' '.join(str(e) for e in st.cartesian_product())

c_p_d = c_p.replace("[","{")
cp_style = c_p_d.replace("]","}")

print(cp_style)

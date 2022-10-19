from set_theory import *

A = "1,2,3,4"
B = "0,5,6,7"

st = SetTheory(A,B)

print('###DISPLAY###')
print(st.display())
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

print('###POWER SET A###')
print(st.power_set(A))

print('###POWER SET B###')
print(st.power_set(B))



from set_theory import *

A = "DD"
B = "AA,BB,CC"

st = SetTheory(A,B)

print('###DISPLAY###')
print(st.display())
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

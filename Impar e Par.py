lista = []
par = []
impar = [] 

for k in range (10):
    num = int (raw_input())
    lista.append(num)

for i in range(len (lista)):
    if lista[i]%2 == 0:
       par.append(lista [i])
    else:
       impar.append (lista [i])

print 'Lista toda:', lista
print 'Lista de par:', par
print 'Lista de impar:', impar
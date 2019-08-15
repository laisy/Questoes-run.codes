num = float (raw_input())

soma = 0
acima = 0
abaixo = 0
lista = [num]
qtd = 1

while num != -1:
    num = float (raw_input())
    if num != -1:
        lista.append(num)
        qtd += 1

print qtd 

print ' '.join(map(str, lista))

for k in range(len(lista)):
        soma += lista[k]
        media = soma / len(lista)
        if lista[k] < 9:
            abaixo +=1

for n in range(len(lista)):
     if lista[n] > media:
            acima+= 1
            
lista.reverse()
for n in lista:
    print n
print soma
print '%.2f' % media
print acima
print abaixo
print 'Fim.'
        
            
    

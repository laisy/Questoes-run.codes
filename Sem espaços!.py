palavra = raw_input ()
stringvazia = ''
soma = 0


for k in range(len(palavra)):
    if palavra[k] != ' ':
        stringvazia = stringvazia + palavra[k]
        soma = soma + 1

print 'Sem espaco:', stringvazia         
print 'Tamanho:', soma




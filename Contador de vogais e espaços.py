palavra = raw_input ()
soma1 = 0
soma2 = 0

for k in range(len(palavra)):
    if palavra[k] == ' ':
        soma2 = soma2 + 1
print 'Espacos:', soma2
for k in range(len(palavra)):
    if palavra[k] == 'a' or palavra[k] == 'e' or palavra[k] == 'i' or palavra[k] == 'o' or palavra[k] == 'u'or palavra[k] == 'A'or palavra[k] == 'E'or palavra[k] == 'I' or palavra[k] == 'O' or palavra[k] == 'U':
            soma1 = soma1 + 1
print 'Vogais:', soma1

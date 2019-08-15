x = input()
y = input()

contador = 0

for k in range(len(x)):
    for n in range(len(y)):
        if x[k] == y[n]:
            contador += 1

print 'As listas tem', contador, 'elementos em comum.'


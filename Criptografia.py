texto = str (raw_input ())

texto2 = ''

for k in range(len(texto)):
    posicao = ord(texto[k]) + 3
    texto2 = texto2 + str(unichr(posicao))

print texto2[::-1]

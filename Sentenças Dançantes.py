entrada = raw_input()
saida = ''
esp = 0

for k in range(len(entrada)):
    
    if (entrada[k] == ' '):
        esp += 1
        saida += ' '
            
    else:
        if(esp == 0):
            if(k % 2 == 0):
                saida = saida + entrada[k].upper()
            else :
                saida = saida + entrada[k].lower()
           
        else:
            if(esp % 2 != 0):
                if(k % 2 ==0):
                    saida = saida + entrada[k].lower()
                else:
                    saida = saida + entrada[k].upper()
            else:
                if(k % 2 == 0):
                    saida = saida + entrada[k].upper()
                else:
                    saida = saida + entrada[k].lower()
print saida
                

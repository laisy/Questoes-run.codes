num = raw_input()

flag = True
soma = 0

for k in range(len(num)):
        soma += int(num[k])
        if soma % 2 == 0:
            flag = True
        for i in range(len(num)-1):
                if num[i] == num[i+1]:
                    flag = False
                if num[i] == num[-1]:
                    flag = False
                if len(num) != 6:
                    flag =  False

if flag == True:
    print 'Numero valido!'
else:
    print 'Numero invalido!'

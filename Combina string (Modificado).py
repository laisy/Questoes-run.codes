x = raw_input ()
y = raw_input ()
xy = ''
count = ()
resto = ''

if len(x) < len(y):
    resto = y[len(x):]
            
else:
    resto = x[len(y):]

if len(x) < len(y):
    count = len(x)
else:
    count = len(y)

for k in range(count):
    s1 = x[k]
    s2 = y[k]
    xy = xy + s1
    xy = xy + s2 



print xy+resto
                        

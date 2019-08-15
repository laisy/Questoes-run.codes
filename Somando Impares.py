
A = int (raw_input ())
B = int (raw_input ())

soma = 0

for k in range (A+1,B):
    if k % 2 == 1:

        soma = soma + k

print soma 

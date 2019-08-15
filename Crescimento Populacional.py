A= float(raw_input ())
B= float (raw_input ())

anos = 0

while A<B:
     A = A + A*0.03
     B = B + B*0.015
     anos = anos + 1

print anos, 'anos'

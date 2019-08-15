n1= float (raw_input ())
n2= float (raw_input ())
media= (n1+n2)/2

if media>=9.0:
    print 'EXCEPCIONAL'
elif media>=7.5 and media<9:
    print 'APROVADO'
elif media>=6.0 and media<7.5:
    print 'APROVADO'
elif media>=4.0 and media<6:
    print 'REPROVADO'
else:
    print'REPROVADO'

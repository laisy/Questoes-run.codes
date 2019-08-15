cigarros = float (raw_input ())
meses = float (raw_input ())

horas = (cigarros*20)/60
dias = (horas*(meses*30))/24

print 'Perdeu: %.2f' %dias, 'dias de vida'


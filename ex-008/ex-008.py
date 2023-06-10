
# Conversor de Medidas
print('\033[32m#008 \033[33m- Conversor de Medidas\033[m')

medida = float(input('\033[46mDigite uma medida em metros: \033[m'))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
hm = medida / 100
dam = medida / 10
print('\033[32;1m{}m\033[m\033[31m em suas conversões: \033[32;1m\n{}cm \n{}mm \n{}dm \n{}km \n{}hm \n{}dam\033[m'.format(medida, cm, mm, dm, km, hm, dam))

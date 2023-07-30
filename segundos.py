
segundos_str =input ("Por favor, entre com o número de segundos que deseja converter:")
segundos_int = (int(segundos_str))

a = segundos_int // 86400
a_resto = segundos_int % 86400
b = a_resto // 3600
b_resto = a_resto % 3600
c = b_resto // 60
d = b_resto % 60

print (a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")

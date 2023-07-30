
segundos_str =input ("QUANTOS SEGUNDOS DESEJA CONVERTER? ")
segundos_int = (int(segundos_str))

dias = segundos_int // 86400
diasresto = segundos_int % 86400
horas = diasresto // 3600
horasresto = diasresto % 3600
minutos = horasresto // 60
minutosresto = horasresto % 60

print ( "ISSO RESULTA EM: ", dias, "Dias,", horas, "Horas,", minutos, "minutos e", minutosresto, "segundos.")

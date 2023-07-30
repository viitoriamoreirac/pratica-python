dinheiro_gasto = int( input("Quanto você gastou?"))
quantia = int( input("Quanto você recebeu?"))
total_restante = quantia - dinheiro_gasto

if total_restante >= 0:
   print ("Sobrou dinheiro.")
else:
   print ("Você gastou mais do que deveria.")

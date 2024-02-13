stock=100
valorinicial=80
porcentaje=float(input("Introduce percentage valor for 3% introduce 2.99: "))
if stock > valorinicial and porcentaje<stock*0.03 and stock*0.03>valorinicial*0.03:
    print(stock*0.03)
    print(valorinicial * 0.03)
    print("sell")
#todo Hacer que recoja datos de la pahina bybit para comprobar precio y transacciones
elif stock < valorinicial:
    print("buy")
else:
    print("nothing")
    print(stock * 0.03)
    print(valorinicial * 0.03)

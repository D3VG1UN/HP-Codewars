prestamo=240000
interes_anual=4
interes_mensual=interes_anual/(100*12)

meses_prestamo=int(input("Cuántos meses recibirás el préstamo?: "))
pagamento_mensual=(prestamo*interes_mensual)/(1-(1+interes_mensual)**-meses_prestamo)

print(round(pagamento_mensual, 2))
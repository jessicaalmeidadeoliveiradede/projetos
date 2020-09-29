dia=int(input("quantos dia alugados"))
km=float(input("quantos km rodado"))
pago=(dia*60)+(km*0.15)
print("o total a pagar e de R${:.2f}".format(pago))
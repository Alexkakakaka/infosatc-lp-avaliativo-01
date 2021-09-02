real=float(input("Quantos dinheiro na carteira eu tenho? R$"))
dolar = real/5.41
print("Com R${:.2f} Você pode comprar US${:.2f}".format(real,dolar))
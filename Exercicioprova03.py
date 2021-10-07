altura = float(input("Digite a altura da parede em metros: "))
comprimento = float(input("Digite o comprimento : "))
area = altura*comprimento
comprimento = area / 3
litros = comprimento / 3.6
total = litros*107.00
print("Você terá que comprar um total de {} litros de tinta valor {}".format(litros, total))

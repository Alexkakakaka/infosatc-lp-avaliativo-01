valor = float(input("Digite o valor do premio:"))
imposto = valor- 7/100
valornovo = valor - imposto
primeiro= valornovo * 46/100
segundo = valornovo * 32/100
terceiro = valornovo - (primeiro + segundo)
print("o Premio foi de r$ {}, o valor desconto ficou R$ {} o imposto ficou R$ {}".format(valor, valornovo, imposto))
print("O primeiro ganhador ganhou R$ {}, o segundo ganhaou R$ {} eo terceiro ganhador ganhou R$ {}".format(primeiro, segundo, terceiro))

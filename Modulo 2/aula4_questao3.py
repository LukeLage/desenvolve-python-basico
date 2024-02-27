nome_produto1 = input('Digite o nome do produto 1: \n')
preco_produto1 = float(input('Digite o preço unitário do produto 1: \n'))
quantidade_produto1 = int(input('Digite a quantidade do produto 1: \n'))
preco1 = preco_produto1 * quantidade_produto1

nome_produto2 = input("Digite o nome do produto 2: \n")
preco_produto2 = float(input("Digite o preço unitário do produto 2: \n"))
quantidade_produto2 = int(input("Digite a quantidade do produto 2: \n"))
preco2 = preco_produto2 * quantidade_produto2

nome_produto3 = input("Digite o nome do produto 3: \n")
preco_produto3 = float(input("Digite o preço unitário do produto 3: \n"))
quantidade_produto3 = int(input("Digite a quantidade do produto 3: \n"))
preco3 = preco_produto3 * quantidade_produto3

preco_total = preco1 + preco2 + preco3

print('Total: R$ {:.2f}' .format(preco_total))
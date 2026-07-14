print("Bem-vindo ao sistema digital da lanchonete")
nome = input("Digite seu nome: ")
lanche = input("Qual lanche você gostaria de pedir?")
quantidade = int(input("quantos lancher você deseja? "))
preco_unitario = 15.00
total = quantidade * preco_unitario

print("-" * 40)
print("Resumo do pedido:")
print("Cliente:", nome)
print("Lanche:", lanche)
print("Quantidade:", quantidade)
print("Total a pagar: R$ {:.2f}".format(total))
print("Obrigado por usar nosso sistema, volte sempre!")
print("-" * 40)


lanches = {'1': ('Hambürgüer', 20), '2': ('Cheeseburgüer', 22), '3': ('Veggie', 18), '4': ('Frango', 1)}
bebidas = {'1': ('Refrigerante', 6), '2': ('Suco', 8), '3': ('Água', 4)}
adicionais = {'1': ('Batata Frita', 10), '2': ('Sobremesa', 12)}

print("Lanches disponiveis:")
for k, v in lanches.items():
    print(f"{k} - {v[0]} (R${v[1]})")
print("\nBebidas disponiveis:")
for k, v in bebidas.items():
    print(f"{k} - {v[0]} (R${v[1]})")
print("\nAdicionais:")
for k, v in adicionais.items():
    print(f"{k} - {v[0]} (R${v[1]})")

lanche_escolhido = input("Digite o número do lanche: ")
bebida_escolhida = input("Digite o número da bebida: ")
adicional_escolhido = input("Digite o número do adicional (ou 0 para nenhum): ")

total = 0
total += lanches[lanche_escolhido][1]
total += bebidas[bebida_escolhida][1]
if adicional_escolhido != '0':
    total += adicionais[adicional_escolhido][1]

if adicional_escolhido != '0':
    desconto = total * 0.10
    total -= desconto
    print(f"Desconto de 10% aplicado! (-R${desconto:.2f})")

if total >= 50:
    print("Parabéns! Você ganhou uma sobremesa grátis!")
else:
    print("Você não ganhou uma sobremesa grátis!")

if adicional_escolhido == '0':
    print("Dica: peça um adicional na próxima vez para ganhar desconto!")


print(f"Total do pedido: R${total:.2f}")


if lanche_escolhido not in lanches or bebida_escolhida not in bebidas or (adicional_escolhido not in adicionais and adicional_escolhido != '0'):
    print("Opção inválida! Tente novamente.")
    exit()


nome = input("Digite seu nome: ")
print(f"\nObrigado pelo pedido, {nome}! Volte sempre!")

print("-" * 30)

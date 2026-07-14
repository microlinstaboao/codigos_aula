# Constantes
TAXA_SERVICO = 0.1  # 10% de taxa de serviço

# Variáveis
nome_cliente = "Marcos"
produto = "Sanduíche"
preco_unitario = 12.50
quantidade = 2

# Cálculo do valor total sem taxa
valor_total = preco_unitario * quantidade

# Cálculo da taxa de serviço
taxa = valor_total * TAXA_SERVICO

# Cálculo do valor final
valor_final = valor_total + taxa

# Impressão das informações
print("Cliente:", nome_cliente)
print("Produto:", produto)
print("Quantidade:", quantidade)
print("Valor total sem taxa: R$", valor_total)
print("Taxa de serviço (10%): R$", taxa)
print("Valor final a pagar: R$", valor_final)

pagamento_em_dinhheiro = 30.00
troco = pagamento_em_dinhheiro - valor_final
print("troco: R$", troco)
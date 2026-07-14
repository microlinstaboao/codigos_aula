nome = input("Informe seu nome: ")
senha = input("Digite sua senha (4 dígitos): ")

#Verificação da senha
if senha != "1234":
    print("⚠️ Acesso negado! Senha incorreta.")
    exit() # Encerra o programa se a senha estiver errada

#Solicitação do saldo e valor do saque
saldo = float(input("Informe seu saldo disponível: R"))
saque = float(input("Digiteovalorquedesejasacar:R"))

#Verifica se o valor é válido
if saque <= 0:
    print("⚠️ Valor inválido! O valor do saque deve ser maior que zero.")
    exit()

#Verifica se o cliente possui token
tem_token = input("Você possui token de segurança ativo? (sim/não): ").strip().lower()

print(f"\nOlá, {nome}! Estamos analisando sua solicitação...\n")

if saque > saldo:
    print("✖ Saque negado! Você não tem saldo suficiente.")
elif saque > 5000:
    print("⧫ Saque negado! O valor ultrapassa o limite máximo permitido por saque.")
elif saque > 1000:
    if tem_token == "sim":
        print("✔ Saque autorizado! Validação com token concluída com sucesso. Retire seu dinheiro 🏦")
    else:
        print("⧫ Saque negado! Você precisa ativar seu token para sacar esse valor.")
else:
        print("✔ Saque autorizado com sucesso! Retire seu dinheiro 🏦")

print("\n ⧫ Obrigado por utilizar o TechBank. Volte sempre!")
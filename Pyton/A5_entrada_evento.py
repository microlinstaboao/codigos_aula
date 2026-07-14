idade = int(input("Digite sua idade: "))
tem_documento = input("Está com o documento? (sim/não): ").lower() == "sim"
tem_autorizacao = input("Possui autorização? (sim/não): ").lower() == "sim"
cadastro_realizado = input("Cadastro foi realizado? (sim/não): ").lower() == "sim"
if (idade >= 18 or (tem_documento and tem_autorizacao)) and cadastro_realizado:
    print("Acesso permitido. Bem-vindo ao evento!")
else:
    print("Acesso negado. Verifique os requisitos de entrada.")

if not cadastro_realizado:
    print("Acesso negado: cadastro não encontrado.")
elif idade < 18 and not (tem_documento and tem_autorizacao):
    print("Acesso negado: menor de idade sem documentação completa.")
else:
    print("Acesso permitido. Aproveite o evento!")
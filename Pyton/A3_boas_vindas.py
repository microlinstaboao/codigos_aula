nome = input("Olá qual é o seu nome: ")

# Conversão da idade para número inteiro
idade = int(input("Olá qual a sua idade: "))
cidade = input("Onde você mora?: ")
hobby = input("Qual é o seu hobby: ")

# Cálculo da Idade do aluno em 2030
idade_2030 = idade + (2030-2025)

# Mensagem Personalizada
print("Olá,", nome + "!")
print("Que legal saber que você tem", idade, "anos e mora em", cidade + ".")
print("Gostamos muito de pessoas que curtem", hobby + "!")
print("em 2030 você terá", idade_2030, "anos.")
print("Esperamos que você aproveite ao máximo nossos serviços, "+ nome +"!")


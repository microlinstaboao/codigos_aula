senha_correta = "python123"  # Senha que o usuário precisa acertar
tentativas = 0               # Contador de tentativas realizadas
limite = 3                   # Número máximo de tentativas permitidas

# LOOP PRINCIPAL - ENQUANTO O USUÁRIO TIVER TENTATIVAS
# ============================================
# O loop vai executar enquanto o número de tentativas for menor que o limite
while tentativas < limite:
    
    # SOLICITA A SENHA AO USUÁRIO
    # ============================================
    # input() captura o que o usuário digita
    # .strip() remove espaços extras no início e fim
    senha_digitada = input("Digite sua senha: ").strip()
    
    # VERIFICA SE A SENHA ESTÁ CORRETA
    # ============================================
    # Compara a senha digitada com a senha correta
    if senha_digitada == senha_correta:
        # Se for igual, exibe mensagem de sucesso
        print("Acesso autorizado!")
        # break interrompe o loop imediatamente
        break
    else:
        # Se for diferente, exibe mensagem de erro
        print("Senha incorreta.")
        # Incrementa o contador de tentativas (+1)
        tentativas += 1

# VERIFICA SE AS TENTATIVAS ACABARAM
# ============================================
# Se o número de tentativas atingiu o limite máximo
if tentativas == limite:
    # Exibe mensagem de bloqueio
    print("Número de tentativas excedido. Acesso bloqueado.")

# MENSAGEM FINAL
# ============================================
# Esta linha sempre será executada, independente do resultado
print("Fim do programa.")
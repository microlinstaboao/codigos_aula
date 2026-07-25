senha_correta = "dragao98"   # Senha secreta para abrir o cofre
tentativas = 0               # Contador de tentativas
limite = 3                   # Máximo de 3 tentativas

# LOOP DE TENTATIVAS
# ============================================
while tentativas < limite:
    
    # SOLICITA A SENHA COM MENSAGEM TEMÁTICA
    # ============================================
    senha_digitada = input("Acesso restrito! Digite a senha para abrir o cofre: ")
    
    # VERIFICA SE A SENHA ESTÁ CORRETA
    # ============================================
    if senha_digitada == senha_correta:
        # Senha correta - cofre aberto
        print("Cofre aberto com sucesso. Bem-vindo ao sistema!")
        # Sai do loop
        break
    else:
        # Senha incorreta - alerta
        print("Senha incorreta! O alarme será ativado se errar novamente.")
        # Conta mais uma tentativa
        tentativas += 1

# VERIFICA BLOQUEIO POR TENTATIVAS EXCEDIDAS
# ============================================
if tentativas == limite:
    print("Tentativas esgotadas. Cofre bloqueado por segurança.")

# MENSAGEM DE ENCERRAMENTO
# ============================================
print("Obrigado por tentar acessar o sistema. Até logo!")

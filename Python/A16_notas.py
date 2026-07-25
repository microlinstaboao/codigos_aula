# ============================================
# SISTEMA COMPLETO DE CADASTRO DE NOTAS
# ============================================

# VARIÁVEIS GLOBAIS
# ============================================
alunos = []
notas = []

# ENTRADA DE DADOS INICIAL
# ============================================
qtd_alunos = int(input("Digite o número de alunos: "))
qtd_disciplinas = int(input("Digite o número de disciplinas: "))

# FUNÇÃO PARA CADASTRAR NOTAS
# ============================================
def cadastrar_notas(qtd_alunos, qtd_disciplinas):
    alunos = []
    notas = []
    
    for i in range(qtd_alunos):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        alunos.append(nome)
        
        notas_aluno = []
        for j in range(qtd_disciplinas):
            nota = float(input(f"Digite a nota {j+1} de {nome}: "))
            notas_aluno.append(nota)
        notas.append(notas_aluno)
    
    return alunos, notas

# FUNÇÃO PARA CALCULAR MÉDIA
# ============================================
def calcular_media(notas_aluno):
    return sum(notas_aluno) / len(notas_aluno)

# FUNÇÃO PARA ENCONTRAR A MAIOR NOTA
# ============================================
def maior_nota(matriz_notas):
    maior = -1
    aluno_maior = ""
    disc_maior = 0
    
    for i in range(len(matriz_notas)):
        for j in range(len(matriz_notas[i])):
            if matriz_notas[i][j] > maior:
                maior = matriz_notas[i][j]
                aluno_maior = alunos[i]
                disc_maior = j + 1
    
    return aluno_maior, disc_maior, maior

# FUNÇÃO PARA EXIBIR RELATÓRIO
# ============================================
def exibir_relatorio(alunos, notas):
    print("\n--- RELATÓRIO FINAL ---\n")
    for i in range(len(alunos)):
        media = calcular_media(notas[i])
        print(f"Aluno: {alunos[i]}")
        print(f"Notas: {notas[i]}")
        print(f"Média: {media:.2f}\n")

# FUNÇÃO PARA VALIDAR NOTA (CORRIGIDA)
# ============================================
def validar_nota():
    while True:
        nota = float(input("Digite a nota (0 a 10): "))
        if 0 <= nota <= 10:  # Corrigido: "b" para "0"
            return nota
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")  # Corrigido: removido "A"

# FUNÇÃO PARA CALCULAR MÉDIA POR DISCIPLINA
# ============================================
def media_por_disciplina(notas):
    qtd_disciplinas = len(notas[0])
    qtd_alunos = len(notas)
    
    print("\n\n Média por disciplina:")
    for i in range(qtd_disciplinas):
        soma = 0
        for j in range(qtd_alunos):
            soma += notas[j][i]
        media = soma / qtd_alunos
        print(f"Disciplina {i + 1}: {media:.2f}")

# FUNÇÃO PARA BUSCAR ALUNO
# ============================================
def buscar_aluno(nome_busca, alunos, notas):
    nome_busca = nome_busca.strip().lower()
    encontrado = False
    
    for i in range(len(alunos)):
        if alunos[i].lower() == nome_busca:
            encontrado = True
            print(f"\n Resultado para {alunos[i]}:")
            print("Notas:", notas[i])
            media = sum(notas[i]) / len(notas[i])
            print(f"Média: {media:.2f}")
            break
    
    if not encontrado:
        print("X Aluno não encontrado.")

# FUNÇÃO PARA LINHA SEPARADORA
# ============================================
def linha():
    print("-" * 40)

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

# Cadastra as notas
alunos, notas = cadastrar_notas(qtd_alunos, qtd_disciplinas)

# Exibe o relatório
exibir_relatorio(alunos, notas)

# Exibe a média por disciplina
media_por_disciplina(notas)

# Encontra e exibe a maior nota
aluno, disc, nota = maior_nota(notas)
print(f" 🎉 Maior nota: {nota:.2f} | Aluno: {aluno} | Disciplina: {disc}")

# Busca um aluno específico
nome_digitado = input("\nDigite o nome do aluno para buscar: ")
buscar_aluno(nome_digitado, alunos, notas)

# Linha final
linha()
print("FIM DO PROGRAMA")
linha()
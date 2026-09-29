import time

# --- VARIÁVEIS DE CONTROLE E PONTUAÇÃO ---
jogar_novamente = True
pontuacao_j1 = 0
pontuacao_j2 = 0

print("-" * 40)
print(f"{'BEM-VINDO AO JOKENPÔ EM PYTHON!':^40}")
print("-" * 40)

# --- LAÇO PRINCIPAL DO JOGO (WHILE) ---
while jogar_novamente:

    # --- ENTRADA DE DADOS ---
    print("\nOpções válidas: [pedra], [papel] ou [tesoura]")

    # Convertendo para minúsculas e removendo espaços para evitar erros de digitação
    escolha_j1 = input("Jogador 1, digite sua escolha: ").strip().lower()

    # Truque simples para "esconder" a escolha do Jogador 1 no mesmo terminal
    print("\n" * 20)
    print("--- (Tela limpa para o Jogador 2 não ver a escolha) ---")

    escolha_j2 = input("Jogador 2, digite sua escolha: ").strip().lower()

    # --- SUSPENSE COM LAÇO DE REPETIÇÃO (FOR) ---
    print("\nProcessando a batalha...")
    # O FOR vai contar de 3 até 1, criando uma pausa de 1 segundo entre eles
    for numero in range(3, 0, -1):
        print(f"{numero}...")
        time.sleep(1)  # Pausa a execução por 1 segundo

    print(f"\n>>> Jogador 1 ({escolha_j1}) VS Jogador 2 ({escolha_j2}) <<<\n")

    # --- PROCESSAMENTO E LÓGICA DE VITÓRIA (IF-ELIF-ELSE + OPERADORES) ---
    # 1. Validando se as entradas estão corretas usando o operador lógico OR
    opcoes_validas = ["pedra", "papel", "tesoura"]
    if (escolha_j1 not in opcoes_validas) or (escolha_j2 not in opcoes_validas):
        print("Erro: Um dos jogadores digitou uma opção inválida. Tentem novamente!")

    # 2. Condição de Empate (Operador de igualdade ==)
    elif escolha_j1 == escolha_j2:
        print("Resultado: DEU EMPATE!")

    # 3. Condições de Vitória do Jogador 1 (Uso de operadores AND e OR em conjunto)
    elif (escolha_j1 == "pedra" and escolha_j2 == "tesoura") or \
         (escolha_j1 == "papel" and escolha_j2 == "pedra") or \
         (escolha_j1 == "tesoura" and escolha_j2 == "papel"):
        print("Resultado: JOGADOR 1 VENCEU ESTA RODADA!")
        pontuacao_j1 += 1  # Operador de atribuição composta

    # 4. Se não foi erro, não foi empate e o J1 não venceu... logicamente o J2 venceu
    else:
        print("Resultado: JOGADOR 2 VENCEU ESTA RODADA!")
        pontuacao_j2 += 1

    # --- PLACAR E CONTROLE DO LAÇO ---
    print("-" * 40)
    print(f"PLACAR: Jogador 1 [{pontuacao_j1}] x [{pontuacao_j2}] Jogador 2")
    print("-" * 40)

    # Pergunta se desejam continuar no laço WHILE
    resposta = input(
        "\nDesejam jogar mais uma rodada? (s/n): ").strip().lower()

    if resposta != "s":
        jogar_novamente = False  # Quebra a condição do WHILE


# --- FIM DO PROGRAMA ---
print("\n" + "=" * 40)
print(f"{'FIM DE JOGO! OBRIGADO POR JOGAR.':^40}")
print("=" * 40)

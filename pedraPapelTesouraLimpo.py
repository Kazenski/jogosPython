import time

jogar_novamente = True
pontuacao_j1 = 0
pontuacao_j2 = 0

print("-" * 40)
print(f"{'BEM-VINDO AO JOKENPÔ EM PYTHON!':^40}")
print("-" * 40)

while jogar_novamente:

    print("\nOpções válidas: [pedra], [papel] ou [tesoura]")
    escolha_j1 = input("Jogador 1, digite sua escolha: ").strip().lower()

    print("\n" * 20)
    print("--- (Tela limpa para o Jogador 2 não ver a escolha) ---")

    escolha_j2 = input("Jogador 2, digite sua escolha: ").strip().lower()

    print("\nProcessando a batalha...")
    for numero in range(3, 0, -1):
        print(f"{numero}...")
        time.sleep(1)  

    print(f"\n>>> Jogador 1 ({escolha_j1}) VS Jogador 2 ({escolha_j2}) <<<\n")

    opcoes_validas = ["pedra", "papel", "tesoura"]
    if (escolha_j1 not in opcoes_validas) or (escolha_j2 not in opcoes_validas):
        print("Erro: Um dos jogadores digitou uma opção inválida. Tentem novamente!")

    elif escolha_j1 == escolha_j2:
        print("Resultado: DEU EMPATE!")

    elif (escolha_j1 == "pedra" and escolha_j2 == "tesoura") or \
         (escolha_j1 == "papel" and escolha_j2 == "pedra") or \
         (escolha_j1 == "tesoura" and escolha_j2 == "papel"):
        print("Resultado: JOGADOR 1 VENCEU ESTA RODADA!")
        pontuacao_j1 += 1  
    else:
        print("Resultado: JOGADOR 2 VENCEU ESTA RODADA!")
        pontuacao_j2 += 1

    print("-" * 40)
    print(f"PLACAR: Jogador 1 [{pontuacao_j1}] x [{pontuacao_j2}] Jogador 2")
    print("-" * 40)

    resposta = input(
        "\nDesejam jogar mais uma rodada? (s/n): ").strip().lower()

    if resposta != "s":
        jogar_novamente = False

print("\n" + "=" * 40)
print(f"{'FIM DE JOGO! OBRIGADO POR JOGAR.':^40}")
print("=" * 40)

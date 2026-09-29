import time

# --- FUNÇÕES DO JOGO ---


def exibir_cabecalho():
    """Exibe o título e a formatação inicial do jogo."""
    print("-" * 40)
    print(f"{'BEM-VINDO AO JOKENPÔ EM PYTHON!':^40}")
    print("-" * 40)


def obter_escolha(nome_jogador):
    """Solicita a jogada, formata a string e aplica o truque de limpar a tela para o Jogador 1."""
    print("\nOpções válidas: [pedra], [papel] ou [tesoura]")
    escolha = input(f"{nome_jogador}, digite sua escolha: ").strip().lower()

    if nome_jogador == "Jogador 1":
        print("\n" * 20)
        print("--- (Tela limpa para o Jogador 2 não ver a escolha) ---")

    return escolha


def contagem_suspense():
    """Faz a contagem regressiva usando o laço FOR."""
    print("\nProcessando a batalha...")
    for numero in range(3, 0, -1):
        print(f"{numero}...")
        time.sleep(1)


def determinar_vencedor(escolha_j1, escolha_j2):
    """
    Compara as jogadas e retorna o resultado. 
    Isso ensina aos alunos que funções podem processar dados e 'devolver' (return) uma resposta.
    """
    opcoes_validas = ["pedra", "papel", "tesoura"]

    if (escolha_j1 not in opcoes_validas) or (escolha_j2 not in opcoes_validas):
        return "erro"

    elif escolha_j1 == escolha_j2:
        return "empate"

    elif (escolha_j1 == "pedra" and escolha_j2 == "tesoura") or \
         (escolha_j1 == "papel" and escolha_j2 == "pedra") or \
         (escolha_j1 == "tesoura" and escolha_j2 == "papel"):
        return "vitoria_j1"

    else:
        return "vitoria_j2"


def exibir_placar(p1, p2):
    """Recebe as pontuações como parâmetros e exibe o placar atualizado."""
    print("-" * 40)
    print(f"PLACAR: Jogador 1 [{p1}] x [{p2}] Jogador 2")
    print("-" * 40)


# --- FUNÇÃO PRINCIPAL (MOTOR DO JOGO) ---

def iniciar_jogo():
    """Controla o laço principal (WHILE) e chama as outras funções na ordem certa."""
    pontuacao_j1 = 0
    pontuacao_j2 = 0
    jogar_novamente = True

    exibir_cabecalho()

    while jogar_novamente:
        # Chamando funções e guardando o retorno em variáveis
        escolha_j1 = obter_escolha("Jogador 1")
        escolha_j2 = obter_escolha("Jogador 2")

        contagem_suspense()
        print(
            f"\n>>> Jogador 1 ({escolha_j1}) VS Jogador 2 ({escolha_j2}) <<<\n")

        # Analisando o vencedor
        resultado = determinar_vencedor(escolha_j1, escolha_j2)

        if resultado == "erro":
            print("Erro: Um dos jogadores digitou uma opção inválida. Tentem novamente!")
        elif resultado == "empate":
            print("Resultado: DEU EMPATE!")
        elif resultado == "vitoria_j1":
            print("Resultado: JOGADOR 1 VENCEU ESTA RODADA!")
            pontuacao_j1 += 1
        elif resultado == "vitoria_j2":
            print("Resultado: JOGADOR 2 VENCEU ESTA RODADA!")
            pontuacao_j2 += 1

        exibir_placar(pontuacao_j1, pontuacao_j2)

        resposta = input(
            "\nDesejam jogar mais uma rodada? (s/n): ").strip().lower()
        if resposta != "s":
            jogar_novamente = False

    print("\n" + "=" * 40)
    print(f"{'FIM DE JOGO! OBRIGADO POR JOGAR.':^40}")
    print("=" * 40)


# --- EXECUÇÃO DO SCRIPT ---
# Boa prática em Python: garante que o jogo só rode se o arquivo for executado diretamente
if __name__ == "__main__":
    iniciar_jogo()

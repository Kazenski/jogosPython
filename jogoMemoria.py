import time
import random

# --- VARIÁVEIS DE CONTROLE E LISTAS ---
numeros_secretos = []
palpites_jogador = []
acertos = 0
erros = 0

print("-" * 40)
print(f"{'BEM-VINDO AO JOGO DA MEMÓRIA!':^40}")
print("-" * 40)

# --- GERAÇÃO DOS NÚMEROS (FOR E RANDOM) ---
# O laço FOR vai rodar 5 vezes para sortear 5 números de 1 a 20
for _ in range(5):
    numero_sorteado = random.randint(1, 20)
    numeros_secretos.append(numero_sorteado)  # Adiciona o número na lista

print("\nMemorize a sequência de números abaixo:")
print(f">>> {numeros_secretos} <<<")
print("\nVocê tem 5 segundos...")

# --- SUSPENSE E LIMPEZA DE TELA ---
# O programa pausa por 5 segundos para o jogador decorar
time.sleep(5)

# Limpando a tela com quebras de linha para esconder os números
print("\n" * 50)
print("--- TEMPO ESGOTADO! ---")

# --- ENTRADA DE DADOS DO JOGADOR (FOR) ---
print("\nAgora é sua vez! Digite os números na ordem que apareceram:")

# Coletando os 5 palpites, um por um
for i in range(5):
    # Convertendo a entrada para inteiro (int)
    palpite = int(input(f"Digite o {i+1}º número: "))
    palpites_jogador.append(palpite)  # Guarda o palpite na lista do jogador

# --- PROCESSAMENTO: COMPARANDO AS LISTAS ---
print("\nProcessando seus resultados...")
time.sleep(2)

# Vamos comparar índice por índice (posição por posição) das duas listas
for i in range(5):
    if palpites_jogador[i] == numeros_secretos[i]:
        acertos += 1
    else:
        erros += 1

# --- PLACAR E SAÍDA DE DADOS ---
print("\n" + "=" * 40)
print(f"{'RESULTADO FINAL':^40}")
print("=" * 40)

print(f"Números originais: {numeros_secretos}")
print(f"Seus palpites:     {palpites_jogador}")
print("-" * 40)
print(f"Acertos: {acertos}")
print(f"Erros:   {erros}")

if acertos == 5:
    print("\nParabéns! Você tem uma memória fotográfica!")
elif acertos >= 3:
    print("\nFoi muito bem! Quase acertou tudo.")
else:
    print("\nPrecisa treinar mais a memória!")

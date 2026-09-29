
# 🎮 Jogo Pedra, Papel e Tesoura (Jokenpô) em Python

Bem-vindo ao clássico jogo "Pedra, Papel e Tesoura" construído inteiramente em Python! Este projeto é um excelente laboratório para entendermos na prática como funcionam as entradas de dados, controle de fluxo e laços de repetição na programação.

## 📖 Sobre o Projeto

Este é um jogo para **2 jogadores** operando localmente na mesma máquina. Ele foi desenvolvido utilizando apenas as estruturas fundamentais da linguagem Python, demonstrando como ferramentas simples podem criar uma aplicação interativa e divertida.

---

## 🕹️ Como Jogar

1. Execute o código no terminal do seu VS Code (ou qualquer IDE Python de sua preferência).
2. O **Jogador 1** será solicitado a digitar sua escolha: `pedra`, `papel` ou `tesoura`.
   * [cite_start]*Dica de ouro: Enquanto um jogador digita, o outro deve virar o rosto para não espiar!*
3. Após o Jogador 1 pressionar `ENTER`, o programa limpará a tela automaticamente empurrando o texto para cima, ocultando a jogada.
4. Em seguida, o **Jogador 2** digitará sua escolha.
5. O programa fará uma contagem regressiva dramática de 3 segundos e revelará o grande vencedor da rodada!
6. Um placar será exibido e vocês poderão escolher se desejam jogar mais uma rodada.

---

## 🧠 Como o Código e a Lógica Funcionam

O código foi construído com blocos bem definidos para facilitar o entendimento. Abaixo, detalhamos o coração do nosso programa:

### 1. Variáveis e Tipos de Dados

- **Pontuação:** Utilizamos as variáveis `pontuacao_j1` e `pontuacao_j2` inicializadas como inteiros (`int`) para guardar os pontos.
- **Controle de Estado:** A variável `jogar_novamente` é um valor booleano (`True` ou `False`) que serve como o "interruptor" principal para manter o jogo rodando.

### 2. O Laço Principal (`while`)

- O comando `while jogar_novamente:` cria um ciclo (loop) infinito controlado. Ele atua como o motor do nosso jogo (o famoso *Game Loop*).
- O programa ficará repetindo as rodadas indefinidamente, e só irá parar quando a condição de `jogar_novamente` for alterada para `False` no final do script (quando os jogadores decidirem parar).

### 3. O "Truque" da Limpeza de Tela

- Como os dois jogadores usam o mesmo teclado, aplicamos uma forma criativa de ocultar a jogada do Jogador 1 usando o comando `print("\n" * 20)`[.
- Isso utiliza o operador aritmético de multiplicação (`*`) em uma *String* para imprimir 20 quebras de linha seguidas, "empurrando" as informações anteriores para fora do campo de visão do terminal.

### 4. Contagem Regressiva e Controle de Tempo (`for` e `time`)

- Para criar suspense na revelação, usamos um laço de repetição `for`: `for numero in range(3, 0, -1)`. Isso cria uma contagem decrescente partindo de 3 até chegar a 1.
- Importamos a biblioteca `time` e utilizamos o método `time.sleep(1)` para obrigar a máquina a pausar a execução do programa por exatamente 1 segundo a cada número impresso na tela.

### 5. A Lógica de Decisão (`if - elif - else`)

O processamento para definir quem ganha é o verdadeiro coração do jogo:

- **Prevenção de Bugs:** Começamos com um `if` para validar se os jogadores digitaram as palavras corretamente, evitando que o jogo quebre.
- **Cenário de Empate:** Utilizamos a condição mais simples com o operador de igualdade: `escolha_j1 == escolha_j2`.
- **Vitória do Jogador 1:** Em vez de criarmos vários `ifs` separados, agrupamos **todas** as condições de vitória do Jogador 1 em um único bloco `elif`. Fizemos isso utilizando o operador relacional `==` junto aos operadores lógicos `and` (E) e `or` (OU).
- **Vitória do Jogador 2:** A lógica final usa a técnica de eliminação através do `else`. Se ninguém digitou errado, se não deu empate e se o Jogador 1 não venceu, obrigatoriamente a vitória só pode ser do Jogador 2!

---

*Projeto desenvolvido para fins educacionais nas aulas de Lógica de Programação.*

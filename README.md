
# 🎮 Jogo Pedra, Papel e Tesoura (Jokenpô) em Python

Bem-vindo ao clássico jogo "Pedra, Papel e Tesoura" construído inteiramente em Python! [cite_start]Este projeto é um excelente laboratório para entendermos na prática como funcionam as entradas de dados, controle de fluxo e laços de repetição na programação[cite: 5].

## 📖 Sobre o Projeto

Este é um jogo para **2 jogadores** operando localmente na mesma máquina. Ele foi desenvolvido utilizando apenas as estruturas fundamentais da linguagem Python, demonstrando como ferramentas simples podem criar uma aplicação interativa e divertida.

---

## 🕹️ Como Jogar

1. [cite_start]Execute o código no terminal do seu VS Code (ou qualquer IDE Python de sua preferência)[cite: 9].
2. O **Jogador 1** será solicitado a digitar sua escolha: `pedra`, `papel` ou `tesoura`.
   * [cite_start]*Dica de ouro: Enquanto um jogador digita, o outro deve virar o rosto para não espiar!* [cite: 10]
3. Após o Jogador 1 pressionar `ENTER`, o programa limpará a tela automaticamente empurrando o texto para cima, ocultando a jogada.
4. Em seguida, o **Jogador 2** digitará sua escolha.
5. O programa fará uma contagem regressiva dramática de 3 segundos e revelará o grande vencedor da rodada!
6. Um placar será exibido e vocês poderão escolher se desejam jogar mais uma rodada.

---

## 🧠 Como o Código e a Lógica Funcionam

[cite_start]O código foi construído com blocos bem definidos para facilitar o entendimento[cite: 6]. Abaixo, detalhamos o coração do nosso programa:

### 1. Variáveis e Tipos de Dados

- [cite_start]**Pontuação:** Utilizamos as variáveis `pontuacao_j1` e `pontuacao_j2` inicializadas como inteiros (`int`) para guardar os pontos[cite: 12].
- [cite_start]**Controle de Estado:** A variável `jogar_novamente` é um valor booleano (`True` ou `False`) que serve como o "interruptor" principal para manter o jogo rodando[cite: 12].

### 2. O Laço Principal (`while`)

- O comando `while jogar_novamente:` cria um ciclo (loop) infinito controlado. [cite_start]Ele atua como o motor do nosso jogo (o famoso *Game Loop*)[cite: 13, 15].
- [cite_start]O programa ficará repetindo as rodadas indefinidamente, e só irá parar quando a condição de `jogar_novamente` for alterada para `False` no final do script (quando os jogadores decidirem parar)[cite: 14].

### 3. O "Truque" da Limpeza de Tela

- [cite_start]Como os dois jogadores usam o mesmo teclado, aplicamos uma forma criativa de ocultar a jogada do Jogador 1 usando o comando `print("\n" * 20)`[cite: 16, 17].
- [cite_start]Isso utiliza o operador aritmético de multiplicação (`*`) em uma *String* para imprimir 20 quebras de linha seguidas, "empurrando" as informações anteriores para fora do campo de visão do terminal[cite: 17].

### 4. Contagem Regressiva e Controle de Tempo (`for` e `time`)

- [cite_start]Para criar suspense na revelação, usamos um laço de repetição `for`: `for numero in range(3, 0, -1)`[cite: 18]. [cite_start]Isso cria uma contagem decrescente partindo de 3 até chegar a 1[cite: 18].
- [cite_start]Importamos a biblioteca `time` e utilizamos o método `time.sleep(1)` para obrigar a máquina a pausar a execução do programa por exatamente 1 segundo a cada número impresso na tela[cite: 19].

### 5. A Lógica de Decisão (`if - elif - else`)

[cite_start]O processamento para definir quem ganha é o verdadeiro coração do jogo[cite: 20]:

- [cite_start]**Prevenção de Bugs:** Começamos com um `if` para validar se os jogadores digitaram as palavras corretamente, evitando que o jogo quebre[cite: 20].
- [cite_start]**Cenário de Empate:** Utilizamos a condição mais simples com o operador de igualdade: `escolha_j1 == escolha_j2`[cite: 21].
- [cite_start]**Vitória do Jogador 1:** Em vez de criarmos vários `ifs` separados, agrupamos **todas** as condições de vitória do Jogador 1 em um único bloco `elif`[cite: 22, 23]. [cite_start]Fizemos isso utilizando o operador relacional `==` junto aos operadores lógicos `and` (E) e `or` (OU)[cite: 22].
- **Vitória do Jogador 2:** A lógica final usa a técnica de eliminação através do `else`. [cite_start]Se ninguém digitou errado, se não deu empate e se o Jogador 1 não venceu, obrigatoriamente a vitória só pode ser do Jogador 2! [cite: 24]

---

*Projeto desenvolvido para fins educacionais nas aulas de Lógica de Programação.*

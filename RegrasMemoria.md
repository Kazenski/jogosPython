# 🧠 Jogo da Memória Numérica em Python

Bem-vindo ao Jogo da Memória Numérica! [cite_start]Este projeto é o laboratório perfeito para introduzir o conceito de Listas (Arrays)[cite: 29], além de apresentar aos alunos o uso de novas bibliotecas da linguagem Python.

## 📖 Sobre o Projeto
[cite_start]Neste jogo de memória, o programa exibe 5 números gerados aleatoriamente e, após um curto período, os oculta[cite: 27]. [cite_start]Em seguida, o jogador deve inserir os números que memorizou, um a um, e o sistema mostrará a resposta com a quantidade de acertos e erros[cite: 28]. 

---

## 🕹️ Como Jogar

1. Execute o código no terminal da sua IDE (como o VS Code).
2. O sistema irá sortear e exibir uma sequência de 5 números na tela.
3. **Preste muita atenção:** Você terá apenas 5 segundos para memorizar a sequência exata!
4. Após o tempo esgotar, a tela será limpa automaticamente, escondendo os números.
5. Digite os números na exata ordem em que apareceram, um de cada vez, apertando `ENTER` após cada palpite.
6. O programa processará suas respostas e exibirá o placar final mostrando quantos números você acertou e errou, além de comparar a lista original com os seus palpites.

---

## 🧠 Como o Código e a Lógica Funcionam

[cite_start]O código foi estruturado com blocos bem definidos e separadores visuais[cite: 30]. Abaixo, detalhamos a "mágica" por trás do programa:

### 1. Bibliotecas Importadas (`time` e `random`)
- [cite_start]O programa utiliza a biblioteca `time` para o controle de tempo e pausar o jogo[cite: 31, 32].
- [cite_start]Utilizamos a biblioteca `random` para gerar a sequência[cite: 32]. [cite_start]Especificamente, o comando `random.randint(1, 20)` serve para a máquina escolher um número inteiro aleatório entre 1 e 20[cite: 33].

### 2. O Conceito de Listas (Arrays)
- [cite_start]Diferente de variáveis comuns que guardam apenas um valor por vez, utilizamos as listas `numeros_secretos = []` e `palpites_jogador = []`[cite: 34]. 
- [cite_start]Elas funcionam como "caixas com várias divisórias", sendo capazes de guardar vários números ao mesmo tempo de forma organizada[cite: 34].

### 3. A Função `.append()`
- Para inserir os números sorteados e os palpites dos jogadores dentro de suas respectivas listas, utilizamos a função `.append()`. 
- [cite_start]Toda vez que o comando `append()` é chamado, ele adiciona o valor ao final da fila na lista[cite: 36].

### 4. Limpando a Tela (Ocultando os números)
- [cite_start]Para esconder os números e testar a memória do usuário, reciclamos um "truque" de quebra de linha[cite: 31].
- [cite_start]O comando `print("\n" * 50)` utiliza a multiplicação de Strings para imprimir várias linhas em branco, jogando os números originais para fora da visão do terminal[cite: 37].

### 5. Laços de Repetição (`for`) e Verificação Lógica
- [cite_start]O laço `for i in range(5):` é o ponto crucial da lógica de verificação[cite: 38]. 
- [cite_start]Como temos 5 números, o índice `i` vai variar de 0 até 4[cite: 39]. 
- [cite_start]Assim, o programa compara automaticamente a posição exata da lista de segredos com a mesma posição da lista do jogador (usando a lógica `palpites_jogador[i] == numeros_secretos[i]`)[cite: 39]. [cite_start]Se os números na mesma posição forem iguais, o acerto é contabilizado; caso contrário, é registrado um erro[cite: 39].

---
*Projeto desenvolvido para fins educacionais nas aulas de Lógica de Programação.*
# Expo-2025
Projeto para expo bentinho 2025, feito por Murilo Pereira e Rafael Royer


Jogo de Adivinhação de Números a partir de Palavras

Este é um pequeno jogo de adivinhação em Python onde o usuário deve descobrir um número de 4 dígitos relacionado a uma palavra-chave. O jogo fornece dicas para ajudar a encontrar o número correto, e o estilo de adivinhação lembra o jogo "Termo" (Wordle), mas com números.

Como funciona

O usuário digita uma palavra-chave (que deve estar no dicionário pré-definido).

O programa exibe uma dica sobre o número relacionado a essa palavra.

O usuário tenta adivinhar o número de 4 dígitos com base na dica.

A cada palpite, o programa retorna um feedback colorido:

Verde: Dígito correto e na posição correta.

Amarelo: Dígito correto, mas na posição errada.

Cinza: Dígito incorreto.

O usuário tem até 100 tentativas para acertar o número.

Se acertar, o jogo parabeniza e encerra.

Dicionários usados

palavras_para_numeros: associa palavras a números de 4 dígitos.

dicas: fornece dicas para cada palavra, indicando o intervalo em que o número está.

Como executar

Certifique-se de ter Python instalado (versão 3.x).

Salve o código em um arquivo, por exemplo jogo_numero.py.

Execute no terminal/cmd:

python jogo_numero.py


Digite uma palavra entre as disponíveis:

linguagem

variavel

matematica

hardware

banco de dados

Use as dicas para tentar adivinhar o número.

Exemplo de uso
Digite a palavra descoberta no enigma anterior: linguagem
Dica: O número é menor que 5000.
Tente adivinhar esse número (estilo Termo, com números)!

Digite um número de 4 dígitos: 4821
Resultado: 4 8 2 1
🎉 Parabéns! Você acertou o número, agora lembre deste número para o próximo enigma

Observações

A entrada do número deve ter exatamente 4 dígitos.

Palavras fora do dicionário resultarão em uma mensagem de erro para tentar novamente.

O jogo é case insensitive para a palavra digitada.

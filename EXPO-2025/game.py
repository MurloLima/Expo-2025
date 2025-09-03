palavras_para_numeros = {
    "linguagem": 4821,
    "variavel": 1597,
    "matematica": 7365,
    "hardware": 9043,
    "banco de dados": 6218,
}

dicas = {
    "linguagem": "O número é menor que 5000.",
    "variavel": "O número é menor que 2000 e maior que 1000.",
    "matematica": "O número está entre 7000 e 8000.",
    "hardware": "O número está entre 9000 e 9999.",
    "banco de dados": "O número está entre 5500 e 6500.",
}

VERDE = "\033[92m"
AMARELO = "\033[93m"
CINZA = "\033[90m"
RESET = "\033[0m"

PalavraDigitada = input("Digite a palavra descoberta no enigma anterior: ").lower()

numero_encontrado = None

for palavra in palavras_para_numeros:
    if PalavraDigitada == palavra:
        numero_encontrado = str(palavras_para_numeros[palavra])
        dica = dicas.get(palavra, "")
        break

if numero_encontrado is None:
    print("Palavra não reconhecida. Tente novamente.")

else:
    print(f"Dica: {dica}")
    print("Tente adivinhar esse número (estilo Termo, com números)!\n")

    tentativas = 0
    max_tentativas = 100

    while tentativas < max_tentativas:
        palpite = input("Digite um número de 4 dígitos: ")

        if len(palpite) != 4 or not palpite.isdigit():
            print("Entrada inválida. Digite exatamente 4 dígitos.")
            continue

        resultado_colorido = ""
        numero_temp = list(numero_encontrado)

        for i in range(4):
            if palpite[i] == numero_encontrado[i]:
                resultado_colorido += f"{VERDE}{palpite[i]}{RESET} "
                numero_temp[i] = None
            else:
                resultado_colorido += "_ "

        resultado_final = ""
        for i in range(4):
            if palpite[i] == numero_encontrado[i]:
                resultado_final += f"{VERDE}{palpite[i]}{RESET} "
            elif palpite[i] in numero_temp:
                resultado_final += f"{AMARELO}{palpite[i]}{RESET} "
                numero_temp[numero_temp.index(palpite[i])] = None
            else:
                resultado_final += f"{CINZA}{palpite[i]}{RESET} "

        print("Resultado:", resultado_final.strip())

        if palpite == numero_encontrado:
            print("\n🎉 Parabéns! Você acertou o número, agora lembre deste número para o próximo enigma")
            break

        tentativas += 1
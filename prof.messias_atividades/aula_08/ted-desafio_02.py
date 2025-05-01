# Solicita o número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Nome do arquivo onde será salva a tabuada
nome_arquivo = "tabuada.txt"

# Abre o arquivo para escrita
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(f"Tabuada do {numero}\n")
    arquivo.write("-" * 20 + "\n")
    for i in range(1, 11):
        resultado = numero * i
        linha = f"{numero} x {i} = {resultado}\n"
        arquivo.write(linha)

print(f"Tabuada do {numero} salva no arquivo '{nome_arquivo}' com sucesso!")

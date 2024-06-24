# screva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. 
# Imprima em seguida o caminho completo do arquivo salvo.

# screva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script.
# Imprima em seguida o caminho completo do arquivo salvo.


def salvar_frase_em_arquivo(frase):
    # Obter o caminho do script atual
    import os

    caminho_script = os.path.abspath(__file__)

    # Criar o nome do arquivo (no mesmo local do script)
    nome_arquivo = "frase.txt"
    caminho_completo = os.path.join(os.path.dirname(caminho_script), nome_arquivo)

    # Abrir o arquivo no modo de escrita ("w")
    with open(caminho_completo, "w") as arquivo:
        # Escrever a frase no arquivo
        arquivo.write(frase)

    # Imprimir o caminho completo do arquivo salvo
    print(f"Frase salva em: {caminho_completo}")


# Obter a frase do usuário
frase = input("Digite uma frase: ")

# Salvar a frase no arquivo e imprimir o caminho
salvar_frase_em_arquivo(frase)

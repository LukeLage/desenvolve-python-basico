# Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. 
# Ao final, imprima o conteúdo do arquivo "palavras.txt".

def ler_e_salvar_palavras(arquivo_entrada, arquivo_saida):
  """
  Lê um arquivo de texto, remove espaços em branco e caracteres não alfabéticos, e salva as palavras em outro arquivo, uma por linha.

  Argumentos:
    arquivo_entrada (str): O caminho do arquivo de entrada.
    arquivo_saida (str): O caminho do arquivo de saída.
  """
  # Abrir arquivos de entrada e saída
  with open(arquivo_entrada, "r") as entrada, open(arquivo_saida, "w") as saida:
    # Ler o conteúdo do arquivo de entrada linha por linha
    for linha in entrada:
      # Remover espaços em branco e caracteres não alfabéticos
      palavras = linha.strip().split()
      palavras_sem_especiais = []
      for palavra in palavras:
        palavra_sem_especiais = "".join(caractere.lower() for caractere in palavra if caractere.isalnum())
        if palavra_sem_especiais:
          palavras_sem_especiais.append(palavra_sem_especiais)

      # Escrever cada palavra em uma linha no arquivo de saída
      for palavra in palavras_sem_especiais:
        saida.write(palavra + "\n")

# Obter os caminhos dos arquivos
caminho_frase = "frase.txt"  # Altere para o nome real do arquivo da frase
caminho_palavras = "palavras.txt"

# Ler e salvar as palavras
ler_e_salvar_palavras(caminho_frase, caminho_palavras)

# Imprimir o conteúdo do arquivo "palavras.txt"
with open(caminho_palavras, "r") as arquivo:
  conteudo = arquivo.read()
  print(f"Conteúdo do arquivo 'palavras.txt':\n{conteudo}")

#Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista domínios com o nome principal de todas as URLs, conforme exemplo a seguir.

# Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista domínios com o nome principal de todas as URLs, conforme exemplo a seguir.


def extrair_dominios(urls):
    dominios = []
    for url in urls:
        # Remover "www." e ".com" do URL
        dominio_sem_www_e_com = url[4:-4]

        # Dividir o domínio por pontos (.) para obter o nome principal
        partes_dominio = dominio_sem_www_e_com.split(".")

        # Extrair o nome principal do domínio (primeira parte)
        nome_principal = partes_dominio[0]

        # Adicionar o nome principal à lista de domínios
        dominios.append(nome_principal)

    return dominios


# Exemplo de uso
urls = [
    "www.google.com",
    "www.gmail.com",
    "www.github.com",
    "www.reddit.com",
    "www.yahoo.com",
]
dominios_extraidos = extrair_dominios(urls)
print(f"Domínios extraídos: {dominios_extraidos}")

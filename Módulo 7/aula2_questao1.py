# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 

# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.


def data_por_extenso(data_str):
    # Separar os componentes da data
    try:
        dia, mes, ano = map(int, data_str.split("/"))
    except ValueError:
        return "Data inválida."

    # Verificar se os valores estão dentro dos limites válidos
    if not (1 <= dia <= 31) or not (1 <= mes <= 12) or ano < 1000:
        return "Data inválida."

    # Dicionário com nomes dos meses
    meses_extenso = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }

    # Formatar a data por extenso
    data_extenso = f"{dia} de {meses_extenso[mes]} de {ano}"

    return data_extenso


# Obter a data do usuário
data_str = input("Digite sua data de nascimento no formato (dd/mm/aaaa): \n")

# Converter e imprimir a data por extenso
data_extenso = data_por_extenso(data_str)
if data_extenso != "Data inválida.":
    print(f"Sua data de nascimento por extenso: {data_extenso}")
else:
    print("Formato de data inválido. Por favor, digite no formato dd/mm/aaaa.")

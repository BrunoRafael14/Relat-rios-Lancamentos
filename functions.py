import csv

def cadastrar():
    valor = input("Digite o valor a ser Lançado: ")
    data = input("Digite a data do lançamento (DD/MM/AAAA): ")
    data=data.replace("/", " ").split()

    with open("armazem.csv", "a") as arquivo:
        if arquivo.tell() == 0:
            arquivo.write("Valor,dia,mes,ano\n")
        arquivo.write(f"{valor},{data[0]},{data[1]},{data[2]}\n")

    print("Lançamento cadastrado com sucesso!")
    
def relatorio():
    import matplotlib.pyplot as plt

    print("Qual Período deseja visualizar?")
    print("1 - Mensal")
    print("2 - Anual")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        mes = input("Digite o mês (MM): ")
        ano = input("Digite o ano (AAAA): ")
        with open("armazem.csv", "r") as arquivo: # Pular o cabeçalho
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho
            registros = []
            for linha in leitor:
                registros.append(linha)
            # print(registros)
            for registro in registros:
                if registro[2] == mes and registro[3] == ano:
                    print(f"Valor: {registro[0]}, Data: {registro[1]}/{registro[2]}/{registro[3]}")
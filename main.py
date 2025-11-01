import matplotlib.pyplot as plt
from functions import cadastrar, relatorio

print("Bem vindo ao programa de Relatorios!")
print("Escolha uma opcao:")
print("1 - Cadastrar Lançamento")
print("2 - Relatorio de Lançamentos")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    cadastrar()
elif opcao == 2:
    relatorio()


### desafio 01 - Aula 01

nome=input("Digite o nome: ")
salario=float(input("Digite o salario:"))
percentualbonus=float(input("Digite o bonus:"))
bonus_total= salario * percentualbonus / 100

print(f"Nome: {nome} tem o bonus de  {bonus_total} e salario total de {salario + bonus_total}")
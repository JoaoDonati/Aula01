nome=input("Digite o nome: ")
salario=float(input("Digite o salario:"))
percentualbonus=float(input("Digite o bonus:"))
bonus_total= salario * percentualbonus / 100

###########################
#print("Nome: ", nome)
#print("Total do bonus: ", bonus_total) 
#print("Salario com bonus: ", salario + bonus_total)    
#############################

print(f"Nome: {nome} tem o bonus de  {bonus_total} e salario total de {salario + bonus_total}")
from funcoes import *

usuarios={}
opcao = perguntar()
while (opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L"):
    if (opcao=="I"):
        inserir(usuarios)
    elif (opcao=="E"):
        excluir(usuarios,input("Qual login deseja excluir: "))
    elif (opcao=="P"):
        pesquisar(usuarios,input("Qual login deseja pesquisar: "))
    elif (opcao=="L"):
        listar(usuarios)
    opcao = perguntar()

print(usuarios.items())
print(usuarios.values())
print(usuarios.keys())
print(usuarios.__hash__)
print(usuarios.popitem())
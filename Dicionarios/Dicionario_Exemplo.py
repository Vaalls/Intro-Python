usuarios = {}  #Iniciar um dicionario é melhor colocar em plural variavel
print(usuarios)
usuarios = {
    "chaves": ["Chaves do 8", "24/10/2017", "REP_01"],  #Criando resgistros
    "quico": ["Quico Flores", "24/06/2022", "FIN_01"]
}

print(usuarios)

#Segunda forma de criar registros
usuarios["florinda"] = ["Dona Florinda", "25/10/2023", "FIN_02"]
print(usuarios)

#Buscando por chave
print("*********----*********")
print(usuarios.get("quico"))
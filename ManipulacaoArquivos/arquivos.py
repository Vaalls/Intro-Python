baseDados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo:
        baseDados.append(registro.split(","))

print(baseDados,"\n")
print(baseDados[0][4])
#Junção de Strings ou Contas
print(baseDados[0][0] + baseDados[0][1])
print(float(baseDados[0][0]) + float(baseDados[0][1]))
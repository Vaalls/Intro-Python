tabuada = int(input("Digite qual tabuada você deseja saber.. "))
print("Tabuada do número: " , tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + "x" + str(valor) + " = " + str((tabuada*valor)))
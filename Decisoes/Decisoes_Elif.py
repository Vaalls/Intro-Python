nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
doenca_infectocontagiosa = input("Suspeito de doença infecocontagiosa? ").upper()

if(idade >= 65):
    print("O paciente " + nome + " POSSUI atendimento prioritario")
elif(doenca_infectocontagiosa == "SIM"):
    print("O paciente " + nome + " deve ser direcionado para uma sala reservada")
else:
    print("O paciente " + nome + " pode aguardar na sala comum")
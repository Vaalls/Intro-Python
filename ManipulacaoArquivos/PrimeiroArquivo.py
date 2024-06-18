#arquivo = open("primeiro_arquivo.txt", "w") #criando arquivo
#arquivo.write("Meu primeiro arquivo! AAA que festa!!! UHHUH") #escrevendo no arquivo
#arquivo.close() #fechar arquivo

#Vantagem de escrever desta forma, pois não precisa ficar abrindo e fechando toda vez.
#"w" -> sempre cria um novo arquivo
#"a" -> utiliza o mesmo arquivo e só add
with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nOiii Tudo bem!!!")

#Lendo o arquivo
with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

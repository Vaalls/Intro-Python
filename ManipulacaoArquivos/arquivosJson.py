import json

with open("bd.json", "r") as ar_json:
    dicionario = json.load(ar_json)
    for chave, dados in dicionario.items():
        print(chave, " | ", str(dados))

with open("bd.json", "a") as ar_json:
    chave = "Luana"
    dados = ["Luana", "20", "Pal"]
    jso = {
        chave: dados
    }
    ar_json.write(jso)
    dicionario = json.load(ar_json)
    for chave, dados in dicionario.items():
        print(chave, " | ", str(dados))

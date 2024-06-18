from Funcoes.IdentificacaoDeFuncoes import*

minhaLista = []
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista,30)

print("Excluindo")
excluirPorSerial(minhaLista)

print("Resumindo")
exibirInventario(minhaLista)
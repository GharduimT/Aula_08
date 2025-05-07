'''1)crie um dicionario de nome produto representando com as seguitnes informações:
'nome':'Notebook',
'preco': '3500.00',
'estoque': '15' 

2) logo a baicxo digite o comando para remover a chave estoque.
3) altere o preço
4) imprima o nome e o preço formatado'''


#1)

produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': '15'
}
# print(produto)

#2)
# produto.pop('estoque')
#3)
# print(produto) - fiz errado

produto['preco'] = 4000.00

#4)

print(f"{produto['nome']}: R$ {produto ['preco']}")

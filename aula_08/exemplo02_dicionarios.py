aluno = {
    'Nome': 'Maria',
    'Idade': 29,
    'Curso': 'Análise de Dados'
}

print(aluno)
print(aluno['Nome'])# Eu quero ue printe somente NOME > Leitura(printe dicionário aluno)

aluno ['Nome'] = 'Pedro'
print(aluno)
aluno['E-mail'] = 'pedro@email.com'
print (aluno)

#aluno.pop('') # qual chave eu quero apagar

if 'Tel' in aluno:  #  verifica se uma chave existe
     aluno.pop('E-mail')

print(aluno)

#aluno.clear() - limpa masn ão tira da memoria
#print(aluno)

#del aluno - deixa de existir a variável
#print(aluno)

for chave, valor in aluno.items:  
     print(chave)


#%%
# Imprima na tela os numero de 1 a 10.
# User uma lista para armazenar os numeros
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)

#%%
# Crie uma lista de 5 objetos e
# imprima na tela
objetos = [1, 2, '3', '4', True]
for objeto in objetos:
    print(objeto)

#%%
# Crie duas strings e concatene as duas em uma
# terceira string
texto1 = 'Olá,'
texto2 = ' mundo!'
texto_concatenado = texto1 + texto2

#%%
# Crie uma tupla com os elementos: 1, 2, 2, 3, 4, 4, 4, 5
# depois utilize a função count do objeto
# e verifique quantas vezes aparece o numero 4
tupla = (1, 2, 2, 3, 4, 4, 4, 4, 5)
tupla.count(4)

#%%
# Crie um dicionario vazio e o imprima na tela
dicionario = {}
print(dicionario)

#%%
# Adicione 3 chaves e 3 valores e imprima na tela
dicionario["item_01"] = 1
dicionario["item_02"] = 2
dicionario["item_03"] = 3
print(dicionario)

#%%
# Adicione mais um elemento ao dicionario
dicionario["item_04"] = 4

#%%
# Crie um novo dicionario e 3 elementos.
# Um dos valores deve ser uma lista de elementos numericos
dicionario_2 = { 'item_01': 1, 'item_02': 2, 'item_03': [1, 2, 3]}
print(dicionario_2)

# Considere a string abaixo. Imprima na tela
# apenas os caracteres da posicao 0 à 18
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]



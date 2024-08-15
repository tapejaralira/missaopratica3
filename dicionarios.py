set_inicial = {11, 12, 13, 14}
print(set_inicial)
meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}
print(meu_dicionario)

print(type(meu_dicionario))

for chave in meu_dicionario:
    print(meu_dicionario.get(chave))

print(len(meu_dicionario))

dicionario_frutas = dict({
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
})

print(dicionario_frutas[1])

print(dicionario_frutas[2])

for kay in dicionario_frutas:
    print(dicionario_frutas[kay])

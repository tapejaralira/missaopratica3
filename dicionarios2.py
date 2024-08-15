dicionario = {
    1: {
        'nome': 'Maria',
        'idade': 26,
        'nacionalidade': 'brasileira'
    }
}

dicionario.update({
    2: {
        'nome': 'João',
        'idade': 26,
        'nacionalidade': 'protuguesa'
    },
    3: {
        'nome': 'Ana',
        'idade': 22,
        'nacionalidade': 'argentina'
    }
})

print(dicionario)

copia_dicionario = dicionario.copy()

dicionario.pop(1)
print(dicionario)

dicionario.popitem()
print(dicionario)

dicionario.clear()
copia_dicionario.clear()

novas_chaves = ['a', 'b', 'c,']
novo_dicionario = dict.fromkeys(novas_chaves, 'valor padrão')

print(novo_dicionario.items())
print(novo_dicionario.keys())
print(novo_dicionario.values())

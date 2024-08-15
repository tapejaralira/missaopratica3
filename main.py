from operacoes import calcular_media, verificar_reprovacao, identificar_reprovados

# Estruturas de dados necessárias para armazenar os dados dos alunos e as notas de cada bimestre.
dados_alunos = {
    26: {'nome': 'Maria', 'notas': [8, 7, 5, 9]},
    101: {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
    13: {'nome': 'João', 'notas': [6, 5, 5, 5]},
    37: {'nome': 'Ágatha', 'notas': [8, 6, 7.5, 9]},
    72: {'nome': 'Joaquim', 'notas': [6, 5.5, 5, 7]},
    5: {'nome': 'Félix', 'notas': [10, 8, 8, 8]}
}

matriculas_reprovados = []

# Calcular a média de cada aluno e verificar se foi reprovado
for matricula, info_aluno in dados_alunos.items():
    media = calcular_media(info_aluno['notas'])
    info_aluno['media'] = media
    if verificar_reprovacao(media):
        matriculas_reprovados.append(matricula)

mensagens_reprovados = identificar_reprovados(dados_alunos, matriculas_reprovados)
for mensagem in mensagens_reprovados:
    print(mensagem)

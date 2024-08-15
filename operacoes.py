def calcular_media(notas):
    """
    :param notas: Array contendo as notas dos 4 bimestres de cada aluno
    :return: A média das notas
    """
    return sum(notas) / len(notas)


def verificar_reprovacao(media):
    """
    :param media: Média das notas do aluno.
    :return: True se o aluno foi reprovado (média inferior a 6), False caso aluno aprovado.
    """
    return media < 6


def identificar_reprovados(dados_alunos, matriculas_reprovados):
    """
    :param dados_alunos: Dicionário com os dados dos alunos (matrícula, nome e notas).
    :param matriculas_reprovados: Lista com os números das matrículas dos alunos reprovados.
    :return: Lista de strings com as mensagens dos alunos reprovados.
    """
    mensagens = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        mensagem = f'Alunos Reprovado: {aluno['nome']} - Matrícula: {matricula} - Média Final: {aluno['media']:.2f}'
        mensagens.append(mensagem)
    return mensagens

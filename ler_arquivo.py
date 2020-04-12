"""
Este de as funções para ler os arquivo e criar listar, dicionário
classes, ou o que melhor achar necessário para resolver as questões e somente isso,
ou seja, somente ler o arquivo de texto e salvar em dados python.
"""

arquivo = open('partidos_coligacoes_the_2012.csv', 'r')
coligacoes = []
for i in arquivo:
    coligacao = {'coligacao': i.strip(), 'total_votos':0, 'qtd_vagas':0, 'votos_sobra_total':0}
    coligacoes.append(coligacao)
arquivo.close()

arquivo2 = open('candidatos_e_votos_vereador_THE_2012.csv', 'r')
candidatos = []
for i in arquivo2:
    info_candidato = i.strip().split(';')
    candidato = {'nome': info_candidato[0], 'numero':info_candidato[1],
    'partido':info_candidato[2], 'coligacao':info_candidato[3],
    'total_votos':int(info_candidato[4])}
    candidatos.append(candidato)
arquivo2.close()
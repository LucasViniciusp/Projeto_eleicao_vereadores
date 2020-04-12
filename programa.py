"""
Este arquivo deve conter todas as funções necessárias para resolver
as opçoes do menu do usuário.
"""
from ler_arquivo import candidatos, coligacoes

def contar_votos():
    total_votos = 0
    for i in candidatos:
        total_votos += int((i['total_votos']))
    return total_votos

qe = int(contar_votos() / 29)

def candidatos_do_partido(colig):
    c_partido = []
    for i in candidatos:
        if i['coligacao'] == colig:
            c_partido.append(i)
    return c_partido

def votos_do_partido(colig):
    votos = 0
    for i in candidatos_do_partido(colig):
        votos += i['total_votos']
    return votos

for i in coligacoes:
    i['total_votos'] = votos_do_partido(i['coligacao'])

def vaga(partido):
    qp =  int(votos_do_partido(partido) / qe)
    return qp

for i in coligacoes:   
    i['qtd_vagas'] = vaga(i['coligacao'])

def vagas_sobra():
    vaga_ocupada = 0
    for i in coligacoes:
        vaga_ocupada += i['qtd_vagas']
    vaga_sobra = 29 - vaga_ocupada
    return vaga_sobra

def sobra_votos(partido):
    sobra_votos = votos_do_partido(partido) % qe
    return sobra_votos

for i in coligacoes:
    i['votos_sobra_total'] = sobra_votos(i['coligacao'])

for i in range(vagas_sobra()):
    mais_votos = 0
    colig = ''
    for partido in coligacoes:
        sobra = int(votos_do_partido(partido['coligacao']) / (partido['qtd_vagas'] + 1))
        if sobra > mais_votos:
            mais_votos = sobra
            colig = partido['coligacao']
    for partido in coligacoes:
        if partido['coligacao'] == colig:
            partido['qtd_vagas'] += 1
            break


def eleitos_do_partido(partido):
    disponiveis = candidatos_do_partido(partido)
    c = []
    colig = 0
    for i in coligacoes:
        if i['coligacao'] == partido:
            colig = i
            break
    for i in range(colig['qtd_vagas']):
        mais_votado = 0
        eleito = ''
        for candidato in disponiveis:   
            if candidato['total_votos'] > mais_votado:
                eleito = candidato
                mais_votado = candidato['total_votos']
        c.append(eleito)
        for i in candidatos_do_partido(partido):
            if i == eleito:
                disponiveis.remove(i)
    return c


for partido in coligacoes:
    print('\n', '--------------', partido['coligacao'],'ELEITOS:','--------------', '\n')
    for eleito in eleitos_do_partido(partido['coligacao']):
        print('Nome:', eleito['nome'],'-', eleito['coligacao'],'\n','\t', 'Total de votos:',eleito['total_votos'])
aluno = {}
def notas(*n, sit=False):
    aluno['Total'] = len(n)
    aluno['Maior nota'] = max(n)
    aluno['Menor nota'] = min(n)
    med = 0
    for c in n: #ou aluno['Media'] = sum(n)/len(n)
        med+=c / len(n)
    aluno['Media'] = med
    if sit:
        if aluno['Media'] <= 5:
            aluno['Situação'] = 'Ruim'
        elif 5 < aluno['Media'] < 7:
            aluno['Situação'] = 'Razoável'
        else:
            aluno['Situação'] = 'Boa'
    return aluno


resp = notas(3, 4, 6, 4, 3.3, 10, sit = True)
print(aluno)
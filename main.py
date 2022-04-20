import dados
from sklearn.naive_bayes import GaussianNB   

modelo = GaussianNB()
modelo.fit(dados.atributos, dados.resultados)

febre = int(input('Apresenta febre? '))
cansaco = int(input('Apresenta cansaço? '))
tosseSeca = int(input('Apresenta tosse seca? '))
espirro = int(input('Apresenta espirro? '))
dorNoCorpo = int(input('Apresenta dor no corpo? '))
corizando = int(input('Está corizando? '))
dorDeGarganta = int(input('Apresenta dor de garganta? '))
diarreia = int(input('Apresenta diarréia? '))
dorDeCabeca = int(input('Apresenta dor de cabeça? '))
faltaDeAr = int(input('Apresenta falta de ar? '))

sintomas = [febre, cansaco, tosseSeca, espirro, dorNoCorpo, corizando, dorDeGarganta, diarreia, dorDeCabeca, faltaDeAr]

resultado = modelo.predict([sintomas])

if resultado == 1:
    print('Reagente')
elif resultado == 0:
    print('Não reagente') 

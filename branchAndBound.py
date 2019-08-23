print('Algoritmos de Backtracking')
print('---------- -- ------------\n')
print('Caixeiro Viajante')

solucao = None

def caixeiroBaB(pilha, candidato):
	if len(candidato) == G.n \
	and custo(candidato) < custo(solucao):
		solucao = candidato
		return
	elif custo(candidato) >= custo(solucao):
		return
	for tentativa in naoVisitadas(candidato):
		(p1, c1) = atualiza(pilha, candidato, tentativa)
		caixeiroBaB(p1,c1)
		(pilha, candidato) = restaura(p1, c1)
	return

partida = cidadeInicial()
pilha = pilhaInicial(partida)
candidato = [partida]
caixeiroBaB(pilha, candidato)
print(solucao)
print(custo(solucao))
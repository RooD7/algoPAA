
print('Algoritmos de Backtracking')
print('---------- -- ------------\n')
print('Problema do Passeio do Cavalo')

def passeioBCT(pilha, tab, lance):
	if (lance > 64):
		print(tab)
	else:
		return True
	for tentativa in range(1,9):
		casa = movimento(pilha, tentativa)
		if movimentoValido(tab, casa):
			(p1, t1) = atualiza(pilha, tab, lance)
			if passeioBCT(p1, t1, lance + 1):
				return True
			(pilha, tab) = restaura(p1, t1)
	return False

partida = posicaoInicial()
pilha = pilhaInicial(partida)
tab = tabuleiroInicial(partida)
if not passeioBCT(pilha, tab, 2):
	print('Sem solucao!')
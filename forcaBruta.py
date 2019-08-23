
print('Algoritmos de Forca Bruta')
print('---------- -- ----- -----\n')
print('Subconjuntos')
print('Dado um conjunto de elementos E, enumerar ' +
		'todos os subconjuntos de n elementos formados ' +
		'a partir de E')
def subconjs(E, candidato, n):
	if len(candidato) == n:
		print(candidato)
	elif len(E) > 0:
		subconjs(E[1:], candidato + [E[0]], n)
		subconjs(E[1:], candidato, n)

subconjs([1,2,3,4,5], [], 3)


print('\nPermutacao')
print('Dado um conjunto de elementos E, enumerar ' +
		'todas as permutacoes formadas ' +
		'a partir de E')
def permuta(E, candidato):
	if len(E) == 0:
		print(candidato)
	else:
		for i in E:
			permuta(E - {i}, candidato + [i])

permuta({2,4,5,8},[])
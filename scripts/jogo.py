from tabela import Tabela

from random import choice
from colorama import Style


class Jogo(Tabela):
	def __init__(self):
		Tabela.__init__(self)

		self.perdeu = False
		self.valores = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
		]

		"""self.escreve_tabela(valores=self.valores)

		for tent in range(10):
			self.ColocaAleatório()

		self.Comando('c')

		print('\n' * 10)

		self.escreve_tabela(valores=self.valores)"""


	def Comando(self, comando:str):

		assert comando in 'wasd' # Cima Esquerda Baixo Direita (↑←↓→)


		def Troca(lista, ind, valor):

			lista.pop(ind)
			lista.insert(ind, valor)


		def GeraModificador(valor_comparativo:str, valor_recebido:str):

			# Se for True (1) 1 * 2 - 1 = 1
			# Se for False (0) 0 * 2 - 1 = -1

			return (valor_recebido.lower() == valor_comparativo) * 2 - 1 


		def GeraPercorre(modificador, local_a_percorrer): 
			
			# Por base no modificador, percorre, ou não, a lista ao contrário

			if modificador == -1: percorre = range(len(local_a_percorrer) - 1, 0, -1)
			else: percorre = range(len(local_a_percorrer) - 1)

			return percorre


		def ChecaPresencaInvalida(lista, modificador, indice):
			respostas = []

			possibilidades = [0, modificador]
			for mod in possibilidades: respostas.append(not((indice + mod) in lista))

			return all(respostas)  


		if comando.lower() in 'ad':

			mod = GeraModificador('d', comando)

			for eixo in self.valores: 
				indices_invalidos = []

				percorre = GeraPercorre(mod, eixo)

				for repeticoes in range(len(eixo)):
					for indice in percorre:
				
						if eixo[indice + mod] == ' ':
							Troca(eixo, indice + mod, eixo[indice])
							Troca(eixo, indice, ' ')

							if indice in indices_invalidos: 
								Troca(indices_invalidos, indices_invalidos.index(indice), indice + mod) 

						elif eixo[indice + mod] == eixo[indice] and ChecaPresencaInvalida(indices_invalidos, mod, indice):
							Troca(eixo, indice + mod, 
							self.DeterminaCor(self.IsolaNumero(eixo[indice]) + self.IsolaNumero(eixo[indice + mod]))
							)
							# Resumindo x2
							Troca(eixo, indice, ' ')

							indices_invalidos.append(indice + mod)

		else:

			mod = GeraModificador('s', comando)

			for ind_x in range(len(self.valores[0])): # Largura do primeiro === do resto
				indices_invalidos = []

				percorre = GeraPercorre(mod, self.valores)

				for repeticoes in range(len(self.valores)):
					for ind_y in percorre:	
						
						if self.valores[ind_y + mod][ind_x] == ' ':
							Troca(self.valores[ind_y + mod], ind_x, self.valores[ind_y][ind_x])
							Troca(self.valores[ind_y], ind_x, ' ')

							if ind_y in indices_invalidos: 
								Troca(indices_invalidos, indices_invalidos.index(ind_y), ind_y + mod) 


						elif self.valores[ind_y + mod][ind_x] == self.valores[ind_y][ind_x] and ChecaPresencaInvalida(indices_invalidos, mod, ind_y):
							Troca(self.valores[ind_y + mod], ind_x, 
							self.DeterminaCor(self.IsolaNumero(self.valores[ind_y][ind_x]) + self.IsolaNumero(self.valores[ind_y + mod][ind_x]))
							)
							# Resumindo x2
							Troca(self.valores[ind_y], ind_x, ' ')
							
							indices_invalidos.append(ind_y + mod)


	def ChecaAdicao(self, v_a, v_b):
		if v_a == v_b: return True

		return False


	def ColocaAleatório(self):

		coords = []

		for ind_y, eixos in enumerate(self.valores):
			for ind_x, valor in enumerate(eixos):
				if valor == ' ':
					coords.append((ind_y, ind_x))
					# Coloquei invertido, pq o indice é percorrido invertido


		coord_final = choice(coords)
		valor = self.DeterminaCor(choice((2, 4)))
		#, 8, 16, 32, 64, 128, 256, 512, 1024, 2048))) # → testes
		self.Update(valor, coord_final)


	def Update(self, valor, indice):
		self.valores[indice[0]][indice[1]] = valor

		self.escreve_tabela(valores=self.valores)

if __name__ == '__main__':
    Jogo()
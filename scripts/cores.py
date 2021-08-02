class Cores():
	def __init__(self, valor):
		if type(valor) == str:
			valor = int(valor)

		self.valor = valor

		# Todas as cores ANSI que achei
		self.cores = [cor for cor in range(31, 37)] + [cor for cor in range(91, 97)]

		self.DeterminaCor()

	def DeterminaCor(self):

		cont = 0
		aux = self.valor

		# Procura saber sua potencia de 2
		while aux != 1: 
			aux //= 2
			cont += 1
			
		if cont > len(self.cores):
			cont %= len(self.cores)

		return f'\033[1;{self.cores[cont]}m {self.valor} \033[m'


if __name__ == '__main__':
	import colorama
	colorama.init()

	inst = Cores(131072)
	print(inst.DeterminaCor())

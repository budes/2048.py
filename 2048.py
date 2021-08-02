from sys import path
from os import getcwd, path as path_add

from time import sleep
import colorama

colorama.init()

path.append(path_add.abspath(getcwd() + "\\scripts\\"))
# Coloque o path completo, caso não funcione ↑

from jogo import Jogo


print("""\033[1;32m
    |||||||     ||||||||       ||| |||    ||||||||
   |||   |||   |||    |||     |||  |||   |||    |||
        |||    |||    |||    |||   |||    ||||||||
       |||     |||    |||   ||||||||||   |||    |||
     |||       |||    |||          |||   |||    |||
   |||||||||    ||||||||           |||    ||||||||
\033[m""")

print("Iniciando em", end=" ")

for contagem in range(3):
  #sleep(0.5)
  print("\033[1;33m" + str(contagem + 1), end=" ")
  #sleep(0.5)

print("\033[me já \n \n")



jogo = Jogo()

ContinuarJogo = True

while ContinuarJogo:
	jogo.ColocaAleatório()

	while not jogo.perdeu:
		try:
			
			comando = input("Mover para (↑w ↓s ←a →d): ").strip().lower()[0]
			print("\n")
					
			jogo.Comando(comando)
			jogo.ColocaAleatório()

		except IndexError:
			print("\n Você perdeu!")
			jogo.perdeu = True

			while str(ContinuarJogo) not in "SN":
				ContinuarJogo = input("Deseja continuar? (S/N) ")[0].upper()
				print(ContinuarJogo)

				if ContinuarJogo not in "SN": print("Coloque um valor válido \n")

			if ContinuarJogo in "SN": ContinuarJogo = ContinuarJogo == "S"

			jogo = Jogo()
			continue
      
		except Exception as erro:
			print(erro) 
			print('Comando inválido! \n \n')


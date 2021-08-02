import colorama

class Tabela():
    def __init__(self):

        # Faz o ambiente suportar o ANSI
        colorama.init()

        # Elementos de customização
        self.bordas = ("┌", "┬", "┐", 

                       "├", "┼", "┤", 

                       "└", "┴", "┘")
        
        self.sep_x = '─'
        self.sep_y = '│'

        self.cores = [cor for cor in range(31, 37)] + [cor for cor in range(91, 97)]


    def escreve_tabela(self, larg=None, valores=[]):

        if larg == None:
            larg = len(valores)
            c2 = len(valores[1])

            if c2 > larg: larg = c2

        def DesenheLinha(grau:int, esp:int):
            '''
            grau == 0: SUPERIOR ++
            grau == 1: SEPARADOR
            grau == 2: INFERIOR --
            '''

            grau *= 3

            print(self.bordas[0+grau], end='')
            print(self.sep_x*(esp), end='')
            
            for e in range(len(eixos) - 1):
                print(self.bordas[1+grau], end='')
                print(self.sep_x*(esp), end='')
                
            print(self.bordas[2+grau])



        i = 0
        try:
            maior_larg = len(str(max([self.IsolaNumero(e) for eixo in valores for e in eixo]))) + 1
        except:
            maior_larg = max([len(str(self.IsolaNumero(e))) for eixo in valores for e in eixo])

        esp = 7
        
        if maior_larg > esp:
            esp = maior_larg


        for ind_y, eixos in enumerate(valores):
            for ind_x, elementos in enumerate(eixos):

                i += 1


                # ======= SUPERIOR ++ =======
                if i == 1: 
                    DesenheLinha(0, esp)


                # ======= MEIO =======
                if i < self.conta_tudo(valores) + 1:

                    print(self.sep_y, end='')

                    #print(str(elementos).rjust(esp), end='')
                    #if len(elementos) == maior_larg: print( elementos)
                    
                    print(' ' * (esp-self.conta_caracteres(str(elementos))) + str(elementos), end='')


                if i % larg == 0 and i > 0: 

                    print(self.sep_y, end='\n')


                    # ======= SEPARADOR =======
                    if ind_y != len(eixos) - 1:
                        DesenheLinha(1, esp)

                    # ======= INFERIOR -- =======
                    if ind_y == len(eixos) - 1:
                        DesenheLinha(2, esp)


    def conta_tudo(self, var):
        tot = 0    

        for e in var:
            tot += len(e)

        return tot


    def conta_caracteres(self, var):
        if '\033[' in var:
            return len(var) - 10
        else:
            return len(var)


    def DeterminaCor(self, valor):

        cont = 0
        aux = valor

        # Procura saber sua potencia de 2
        while aux != 1: 
            aux //= 2
            cont += 1
            
        if cont > len(self.cores):
            cont %= len(self.cores)

        return f'\033[1;{self.cores[cont]}m{valor}\033[m'

    def IsolaNumero(self, valor:str):
        valor = list(valor)

        if "\x1b" in valor:
            for i in range(len('\x1b[1;xxm')): valor.pop(0)
            for i in range(len('\x1b[m')): valor.pop(-1)

            retorna = ''
            for e in valor: retorna += e

            return int(retorna)
        else: return valor



if __name__ ==  '__main__':
    tab = Tabela()

    valores_de_teste = [
        ['\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m'],
        ['\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m'],
        ['\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m'],
        ['\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m', '\033[1;32m1\033[m']
    ]
    tab.escreve_tabela(valores=valores_de_teste)
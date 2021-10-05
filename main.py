from insertion_sort import insertion_sort
from RamdomizedSelect import randomizedSelect
from graph import generateGraph


import timeit #lib para calcular tempo
import numpy as np # lib para lidar com arrays
import pandas as pd # lib para montar a tabela
import random # lib para gerar numeros aleatórios


if __name__ == '__main__':
    print("Escolha o valor inicial de entrada: minimo (1)")
    inc = int(input())
    print("Escolha o valor maxímo de entrada: minimo (2000) maximo (20000)")
    max = int(input())
    print("Escolha o valor do passo")
    stp = int(input())

    numLoops = int(max / stp)  # quantidade de vezes em que vai do valor
                               # N que vai no minmo ao maximo
    numbersN = []

    columnsTable = ["k", "kth", "INSERTION", "RSELECT"]

    # array (numbersN) dos N valores (equivalente a coluna N da tabela)
    for x in (range(numLoops)):
        n = inc * (x + 1)
        numbersN.append(n)

    # init table
    table = pd.DataFrame(index=numbersN, columns=columnsTable)
    column = ['INSERTION', 'RSELECT']
    # laço inicial para cada valor de entrada
    for idx, n in enumerate(numbersN):


        arr = np.random.randint(0, 10000, n) # gerando array de numeros inteiros pseudo-aleatoriamente com intervalo de 0 a 10000.
                                             # o parametro (n) significa o tamanho do array


        ## gerando cópias do array original, para nao perder a consistencia, pois os scripts usados alteram o array.
        copyArrayInsert = arr.copy()
        copyArrayRSelect = arr.copy()

        # valor K obtido aleatoriamente, indo de 1 até N
        k = random.randint(1, n)



        # Calculando o tempo utilizado para cada script

        start = timeit.default_timer()
        elementKinsert = insertion_sort(copyArrayInsert, k)
        final = timeit.default_timer()

        timeInsertion = final - start

        start = timeit.default_timer()
        elementKRselect = randomizedSelect(copyArrayRSelect,0, len(arr) - 1, k)
        final = timeit.default_timer()

        timeRSelect = final - start

        # GERANDO TABELA

        table.at[n, 'k'] = k

        table.at[n, 'kth'] = elementKRselect

        table.at[n, 'INSERTION'] = timeInsertion

        table.at[n, "RSELECT"] = timeRSelect





        ## DAVID ::
        '''
            
            Para cada algoritmo, adicione essas linhas:
                    copyArrayNOMEDOALGORTIMO = arr.copy()   
                        
                    start = timeit.default_timer()
                    elementKNOMEDOALGORTIMO = NOMEDOALGORTIMO(PARAMS, K)
                    final = timeit.default_timer()
                    timeNOMEDOALGORIMTO  = final - start
                    
            Ao final, adicione essa linha      
            
                table.at[n, 'NOMEDOALGORIMTO'] = timeNOMEDOALGORIMTO
                
            APOS TUDO ISSO, DEVERÁ APARCER O TEMPO DO ALGORITMO NA TABELA
        '''


    print(table)
    generateGraph(table, numbersN, max)




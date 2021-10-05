from insertion_sort import insertion_sort
from RamdomizedSelect import randomizedSelect

import timeit
import numpy as np
import pandas as pd
import random

from graph import generateGraph

def execFuncSort(index, arr, k):

    auxArray = arr

    if index == 0:
        return insertion_sort(auxArray, k)
    elif index == 1:
        return randomizedSelect(auxArray, 0, len(arr) - 1, k)


if __name__ == '__main__':

    inc = 10
    print("Escolha o valor maxímo de entrada: minimo (2000) maximo (20000)")
    max = int(input())
    stp = 10
    rpt = 1

    numLoops = int(max / stp)
    numbersN = []

    meanOfTimes = np.array([[]])

    columnsTable = ["k", "kth", "INSERTION", "RSELECT"]

    # array dos N valores
    for x in (range(numLoops)):
        n = inc * (x + 1)
        numbersN.append(n)

    listMeanTimes = []

    # init table
    table = pd.DataFrame(index=numbersN, columns=columnsTable)
    column = ['INSERTION', 'RSELECT']
    # laço inicial para cada valor de entrada
    for idx, n in enumerate(numbersN):

        list_of_times = []
        arr = np.random.randint(0, 10000, n)
        copyArrayInsert = arr.copy()
        copyArrayRSelect = arr.copy()
        k = random.randint(1, n)

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




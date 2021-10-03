from insertion_sort import insertion_sort
from RamdomizedSelect import randomizedSelect

import timeit
import numpy as np
import pandas as pd
import random

# from graph import generateGraph


def execFuncSort(index, arr, k):

    if index == 0:
        insertion_sort(arr, k)
    elif index == 1:
        randomizedSelect(arr, 0, len(arr) - 1, k)




# if __name__ == '__main__':
#     a = [1,2,3,4,5]
#     k = insertion_sort(a, k=1)
#     print(k)
if __name__ == '__main__':

    inc = 10
    print("Escolha o valor maxímo de entrada: minimo (2000) maximo (20000)")
    max = int(input())
    stp = 10
    rpt = 1

    numLoops = int(max / stp)
    numbersN = []

    meanOfTimes = np.array([[]])

    columnsTable = ["n", "k", "kth", "INSERTION", "RSELECT"]

    # array dos N valores
    for x in (range(numLoops)):
        n = inc * (x + 1)
        numbersN.append(n)

    listMeanTimes = []

    # init table
    table = pd.DataFrame(index=numbersN, columns=columnsTable)

    # laço inicial para cada valor de entrada
    for idx, n in enumerate(numbersN):
        list_of_times = []
        # laço para cada algoritmo
        for indexAlg, algSort in enumerate(columnsTable):
            # laço para repetir o algoritmo de ordenação
            for x in range(rpt):
                arr = np.random.randint(0, 10000, n)
                k = random.randint(0, n)

                start = timeit.default_timer()
                execFuncSort(indexAlg, arr, k)
                final = timeit.default_timer()

                time = final - start
                list_of_times.append(time)

            #calcula média dos tempos de exução (do laço acima)
            media_time = np.mean(list_of_times)
            listMeanTimes.append(media_time)
            list_of_times.clear()

            ### array of array times to aux craete table

            meanOfTimes = np.concatenate((meanOfTimes, np.array([[round(media_time, 4)]])))

        # GERANDO TABELA

            table.at[n, algSort] = float(meanOfTimes[indexAlg])
    print(table)
#     #generateGraph(table, numbersN, max)




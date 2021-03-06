'''
Abaixo, segue a implementação das estratégias 1, 2, 3.
Tentamos fazer a 4, mas não conseguimos finalizar. Arquivo para o senhor ver a tentativa: select.py
'''

from insertion_sort import insertion_sort
from RamdomizedSelect import randomizedSelect
from graph import generateGraph
from minPriority import FilaMinPrioridade


import timeit #lib para calcular tempo
import numpy as np # lib para lidar com arrays
import pandas as pd # lib para montar a tabela
import random # lib para gerar numeros aleatórios


if __name__ == '__main__':
    print("Escolha o valor inicial de entrada: minimo (1)")
    inc = int(input())
    print("Escolha o valor maxímo de entrada: minimo (100) maximo (2000)")
    max = int(input())
    print("Escolha o valor do passo")
    stp = int(input())

    numLoops = int(max / stp)  # quantidade de vezes em que vai do valor
                               # minimo ao maximo
    numbersN = []

    columnsTable = ["k", "kth", "INSERTION", "MIN_QUEUE", "RSELECT"]

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

        # valor K obtido aleatoriamente, indo de 1 até N
        k = random.randint(1, n)

        ## gerando cópias do array original, para nao perder a consistencia, pois os scripts usados alteram o array.
        copyArrayInsert = arr.copy()
        copyArrayRSelect = arr.copy()

        ### instaciando fila
        queueMin = FilaMinPrioridade()
        # copiando o array gerado aleatoriamente para fila.
        for element in arr:
            queueMin.insert(element)

        # pegando os index reversos, por ex: 5, 4, 3, 2, 1 (para que facilite o o encontro do K menor valor)
        rangeMin = range(queueMin.len())
        reversed_range = reversed(rangeMin)



        start = timeit.default_timer()
        for i in reversed_range:
            if i != k - 1:
                queueMin.delete()

            elif i == k -1:
                elementKminQueue = queueMin.delete()
                print(elementKminQueue, ' Ultimo elemento da excluido da fila de prioridades')
        final = timeit.default_timer()
        timeMinQueue = final - start

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

        table.at[n, "MIN_QUEUE"] = timeMinQueue

    print(table)
    generateGraph(table, numbersN, max)




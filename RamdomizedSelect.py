from RandomizedPartition import  randomizedPartition

def randomizedSelect(array, init, final, k):

    if init == final:
        return array[init]
    ## partition, mesmo algoritmo do quick sort, porem com o pivo pseudo aleatorio.
    q = randomizedPartition(array, init, final)
    i = q - init + 1

    if k == i:
        return array[q]
    ## RECURSAO
    elif k < i:
        return randomizedSelect(array, init, q - 1, k)
    else:
        return randomizedSelect(array, q + 1, final, k - i)
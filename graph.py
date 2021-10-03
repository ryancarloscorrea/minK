# from matplotlib import pyplot as plt
#
#
# def generateGraph(table, listOfN, max):
#
#     plt.ylim(0, 0.15)
#     plt.xlim(0, max)
#
#     plt.xlabel('Tamanho da entrada')
#     plt.ylabel('Tempo')
#     plt.title("Algoritmos de ordenação")
#
#     timesSelection = table['SELECTION'].tolist()
#     timesRadix = table['RADIX'].tolist()
#     timesINSERTION = table['INSERTION'].tolist()
#     timesHEAP = table['HEAP'].tolist()
#     timesMerge = table['MERGE'].tolist()
#     timesShell = table['SHELL'].tolist()
#
#
#     plt.plot(listOfN, timesSelection, label='SELECTION')
#     plt.plot(listOfN, timesRadix, label='RADIX')
#     plt.plot(listOfN, timesINSERTION, label='INSERTION')
#     plt.plot(listOfN, timesHEAP, label='HEAP')
#     plt.plot(listOfN, timesMerge, label='MERGE')
#     plt.plot(listOfN, timesShell, label='SHELL')
#     plt.legend()
#
#     plt.show()
from insertion_sort import insertion_sort

a = [3, 6, 1 , 2 ,10]
k = insertion_sort(a, 4)

print(k)
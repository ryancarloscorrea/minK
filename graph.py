from matplotlib import pyplot as plt


def generateGraph(table, listOfN, max):

    plt.ylim(0, 0.06)
    plt.xlim(0, 200)

    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo')
    plt.title("Algoritmos de ordenação")

    timesRselect = table['RSELECT'].tolist()
    timesINSERTION = table['INSERTION'].tolist()


    plt.plot(listOfN, timesRselect, label='RSELECT')
    plt.plot(listOfN, timesINSERTION, label='INSERTION')


    plt.legend()

    plt.show()

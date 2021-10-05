from matplotlib import pyplot as plt


def generateGraph(table, listOfN, max):

    plt.ylim(0, 0.007)
    plt.xlim(0, max)

    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo')
    plt.title("Min K")

    timesRselect = table['RSELECT'].tolist()
    timesINSERTION = table['INSERTION'].tolist()


    plt.plot(listOfN, timesRselect, label='RSELECT')
    plt.plot(listOfN, timesINSERTION, label='INSERTION')


    plt.legend()

    plt.show()

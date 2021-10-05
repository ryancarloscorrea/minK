from matplotlib import pyplot as plt

'''
script feito para plotar o gráfico automaticamente a partir dos valores gerados na tabela.
'''
def generateGraph(table, listOfN, max):

    plt.ylim(0, 0.007)  # valor limite do eixo Y
    plt.xlim(0, max) # valor limite do eixo X


    # labels e title do gráfico definidos
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo')
    plt.title("Min K")

    #pegando lista dos tempos dos algoritmos
    timesRselect = table['RSELECT'].tolist()
    timesINSERTION = table['INSERTION'].tolist()

    # plotando gráfico
    plt.plot(listOfN, timesRselect, label='RSELECT')
    plt.plot(listOfN, timesINSERTION, label='INSERTION')


    plt.legend()

    plt.show()

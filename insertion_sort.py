def insertion_sort(vetorRecebido, k):
    for index in range(1, len(vetorRecebido)):
        valorAtual = vetorRecebido[index]
        posicaoAtual = index

        while posicaoAtual > 0 and vetorRecebido[posicaoAtual - 1] > valorAtual:
            vetorRecebido[posicaoAtual] = vetorRecebido[posicaoAtual - 1]
            posicaoAtual = posicaoAtual - 1

        vetorRecebido[posicaoAtual] = valorAtual
    return vetorRecebido[k - 1]


class FilaMinPrioridade(object):
    def __init__(self):
        self.queue = []

    #retorna o tamanho da fila
    def len(self):
        return len(self.queue)

    #insere elemento na fila
    def insert(self, data):
        self.queue.append(data)

    #deletando, conforme a min prioridade
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

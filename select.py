'''
Olá professor, não conseguimos finalizar o script do select, mas segua abaixo, para ver que tentamos.
'''


from insertion_sort import insertion_sort

def parttition(A,p,r):
  vetoresComMediana = []
  tetoTamanhoVetor = len(A) / 5
  insertion_sort(A)
  #atribuindo o teto do tamanho do array dividido por 5, a uma variavel
  if tetoTamanhoVetor > 5:
    if tetoTamanhoVetor - round(tetoTamanhoVetor)  > 0 :
        tetoTamanhoVetor = round(tetoTamanhoVetor) + 1
    else:
      tetoTamanhoVetor = (round(tetoTamanhoVetor))
  j = 2
  for j in range (tetoTamanhoVetor):
    vetoresComMediana = A[j]
    insertion_sort(vetoresComMediana)

  parttition(vetoresComMediana,p,r)

def select (A, p, r ,i) :
    if p == r:
	    return A[p]
    q = parttition(A, p,r)
    k = q - p + 1

    if k == i:
        return A[q]

    if k > i  :
        select(A, p, q -1, i)
    else:
        select(A, q + 1, r, i-k)
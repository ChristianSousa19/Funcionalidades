import random
import time


def sorteia(lista):
    for ocnt in range(0,5):
        n=random.randint(1,10)
        lista.append(n)
        print(f"{n}",end="",flush=True)
        time.sleep(1)

def somapar(lista):
    soma=0
    for  valor in lista:
        if valor%2==0:
            soma+=valor
    print(f"Somando os valores pares de {lista} temos {soma}")

numeros=list()
sorteia(numeros)
somapar(numeros)


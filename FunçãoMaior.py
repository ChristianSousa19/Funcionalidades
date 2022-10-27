import time

def maior(*num):
    cont=maior=0
    print("-="*30)
    print("Analisando os valores passados......")
    time.sleep(1.5)
    for valor in num:
        print(f"{valor}",end="",flush=True)
        time.sleep(1)
        if cont==0:
            maior=valor
        else:
         if valor>maior:
            maior=valor
            cont+=1
    print(f"Foram informados {valor} valores ao todo")

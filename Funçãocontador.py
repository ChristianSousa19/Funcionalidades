import time


def contador(i,f,p):
 if p<0:
     p*=1
 if p==0:
     p=1
 print(f"contagem de {i} ate {f}de {p} em {p}")
 time.sleep(1)
 if i<f:
     cont=i
     while cont<=f:
         print(f"{cont}",end=" ",flush=True)
         time.sleep(1)
         cont+=p
     print("FIM")
 else:
     cont=i
     while cont>=f:
      print(f"{cont}",end=" ",flush=True)
      time.sleep(1)
      cont-=p
     print("FIM")

contador(1,10,1)
contador(10,0,2)
print("Agora e sua vez de realizar a contagem")
i=int(input("Inicio: "))
f=int(input("Fim: "))
pa=int(input("Passo: "))
contador(i,f,pa)
for v in range(i,f,pa):
    print(f"{v}",end=" ",flush=True)
    time.sleep(1)





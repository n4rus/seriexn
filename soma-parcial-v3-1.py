#!/usr/bin/env python
# coding: utf-8

# In[10]:


import decimal
from decimal import *

myothercontext = Context(prec=60)

setcontext(myothercontext)


# In[11]:


#cabeçalho obtido do repositorio "inset/intset"
#codigo subsequente deve ser editado
#def: a série "soma xn" é a sequencia de somas parciais de xn"" 
print("Numero inteiro maior que 1")
print("Digite o numero de parcelas xni 'tamanho da série':")

#entrada do tamanho da série
tamanho=input()


# In[12]:


#indice inicial
print("Digite o indice inicial:")
indice=input()


# In[13]:


lista=[]
serie=int(tamanho)
xni=int(indice)

while xni<=serie:
    #soma parcial da sequencia modificada
    if xni <= 1:
        partx=(1/xni)
        #print para testes
        #print(partx)
        lista.append(partx)
        xni=xni+1
    if xni > 1:
        partx=Decimal(partx)+Decimal(1/xni) #decimal.Decimal
        apartx=str(partx)
        lista.append(apartx)
        xni=xni+1


# In[14]:


#adicionar input para print da lista "intervalo"
#print(lista[900000:1000000])
print("Digite o indice inicial a ser exibido (entre " + str(indice) + " e " + str(tamanho) + ").")
indicei=input()
print("Digite o indice final a ser exibido (entre " + str(indicei) + " e " + str(tamanho) + ").")
indicef=input()

indiceff=int(indicef)
indiceii=int(indicei)
printl=lista[indiceii:indiceff]
print("\n" + str(printl))


# In[15]:


#escreve a lista em modo string no arquivo nomeado
demo_file = open('lista.txt','a')
demo_file.write(str(printl))
demo_file.close()


# In[ ]:





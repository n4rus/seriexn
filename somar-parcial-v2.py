#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy


# In[54]:


#cabeçalho obtido do repositorio "inset/intset"
#codigo subsequente deve ser editado
#def: a série "soma xn" é a sequencia de somas parciais de xn"" 
print("Digite o numero de parcelas xni 'tamanho da série':")

#entrada do tamanho da série
tamanho=input()


# In[55]:


#indice inicial
print("Digite o indice inicial")
indice=input()


# In[56]:


lista=[]
serie=numpy.float128(tamanho)
xni=numpy.float128(indice)

listaf=[]

while xni<=serie:
    #soma parcial da sequencia modificada
    if xni <= 1:
        partx=1/xni
        #print para testes
        #print(partx)
        lista.append(partx)
        xni=xni+1
    if xni > 1:
        partx=partx+1/xni
        xni=xni+1
        lista.append(partx)
print(lista[900000:1000000])


# In[57]:


#escreve a lista em modo string no arquivo nomeado
demo_file = open('lista.txt','a')
demo_file.write(str(lista))
demo_file.close()


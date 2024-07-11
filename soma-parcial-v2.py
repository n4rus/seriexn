#!/usr/bin/env python
# coding: utf-8

# In[7]:


#cabeçalho obtido do repositorio "inset/intset"
#codigo subsequente deve ser editado
#def: a série "soma xn" é a sequencia de somas parciais de xn"" 
print("Digite o numero de parcelas xni 'tamanho da série':")

#entrada do tamanho da série
tamanho=input()


# In[8]:


#indice inicial
print("Digite o indice inicial")
indice=input()


# In[9]:


lista=[]
serie=float(tamanho)
xni=float(indice)

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
#adicionar input para print da lista "intervalo"
#print(lista[900000:1000000])
printl=lista[995000:1000000]
print(printl)


# In[10]:


#escreve a lista em modo string no arquivo nomeado
demo_file = open('lista.txt','a')
demo_file.write(str(printl))
demo_file.close()


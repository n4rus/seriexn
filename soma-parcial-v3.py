#!/usr/bin/env python
# coding: utf-8

# In[36]:


#cabeçalho obtido do repositorio "inset/intset"
#codigo subsequente deve ser editado
#def: a série "soma xn" é a sequencia de somas parciais de xn"" 
print("Numero inteiro maior que 1")
print("Digite o numero de parcelas xni 'tamanho da série':")

#entrada do tamanho da série
tamanho=input()


# In[37]:


#indice inicial
print("Digite o indice inicial:")
indice=input()


# In[38]:


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


# In[40]:


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


# In[26]:


#escreve a lista em modo string no arquivo nomeado
demo_file = open('lista.txt','a')
demo_file.write(str(printl))
demo_file.close()


# In[ ]:





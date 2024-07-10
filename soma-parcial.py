#!/usr/bin/env python
# coding: utf-8

# In[59]:


#cabeçalho obtido do repositorio "inset/intset"
#codigo subsequente deve ser editado
#def: a série "soma xn" é a sequencia de somas parciais de xn"" 
print("Digite o numero de parcelas xni 'tamanho da série':")

#entrada do tamanho da série
tamanho=input()


# In[57]:


#indice inicial
print("Digite o indice inicial")
indice=input()


# In[60]:


lista=[]
serie=int(tamanho)
xni=int(indice)

while xni<=serie:
    #soma parcial da sequencia modificada
    parti=0
    partx=parti+1/xni
    #print para testes
    #print(partx)
    lista.append(partx)
    xni=xni+1
print(lista)


# In[65]:


#escreve a lista em modo string no arquivo nomeado
demo_file = open('lista.txt','a')
demo_file.write(str(lista))
demo_file.close()


# In[ ]:





# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:28:13 2022

@author: james
"""

import time

clients=[] #array clientes
contador=[]

nclients=[1350,1080,1104] #NUM CONEXIONES/clientes
DoSClients=[10,12,12]
contAux=[135,90,92]
sleeptimeArray=[0.72,0.79,0.50]
inicio=time.time()



for i  in range(nclients[0]):
    client=i
    clients.append(client)
    
contadorAux=0

while(contadorAux<contAux[0]):
    print("=====")
    for i in range(DoSClients[0]):
        contador=(i+(contadorAux*DoSClients[0]))
        print(i+(contadorAux*DoSClients[0]))
        #time.sleep(0.95)
    print("====fin")
    contadorAux=contadorAux+1
#    if(contadorAux==92):
#        contadorAux=0
        #if(contadorAux==92):
        #    contadorAux=0
fin=time.time()

print(fin-inicio)
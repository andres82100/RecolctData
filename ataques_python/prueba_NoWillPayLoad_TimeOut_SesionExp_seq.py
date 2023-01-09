# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 23:01:35 2022

@author: james
programa secuencial para crean n clientes y conectarlos
conexion de tipo nowillpayload
"""
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes

###DATOS PARA LA CONEXION####
broker = '192.168.100.20'
port = 1883

###### parametros para estadisticas
clients=[] #array clientes

nclients=1024 #NUM CONEXIONES/clientes
keepalive=60    #keep alive
sesionExpira=30 #timeOut


#create clients
for i  in range(nclients):
    ##########asignando id al cliente
   cname=str(i) #ID CLIENTE
   ################creando el cliente MQTT
   client=mqtt.Client(cname, protocol=mqtt.MQTTv5)
   #######TIME OUT
   conn_properties=Properties(PacketTypes.CONNECT)
   conn_properties.SessionExpiryInterval = sesionExpira
   ########### AGREGANDO EL CLIENTE A UN ARRAY
   clients.append(client)

for client in clients:  #RECORRIENDO ARRAY DE CLIENTES
    print(client.connect(broker, port, keepalive, properties=conn_properties)) #CONECTANDO CADA CLIENTE











#while True:
#    for client in clients:  #RECORRIENDO ARRAY DE CLIENTES
#        print(client.connect(broker, port, keepalive, properties=conn_properties)) #CONECTANDO CADA CLIENTE
#    time.sleep(92.3123)
    



#! /usr/bin/env python3
import os
import requests

dir="/data/feedback/"
url= "http://34.67.158.179/feedback/"

for file in os.listdir(dir):
    tipos = ["title","name","date","feedback"]
    datos = {}
    lineas = []
    print(file)
    with open(dir+"/"+file,"r") as txtfile:
        x = 0
        for line in txtfile:
            datos[tipos[x]] = line.rstrip('\n')
            x += 1
    print(datos)

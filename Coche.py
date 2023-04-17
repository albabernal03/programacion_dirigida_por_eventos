from Gaso import *
from Sur import *
from Coche import *
from multiprocessing import Pool
from time import sleep
import time
import random

gasolinera = Gasolinera(1)


class Coche:
    def __init__(self, id):
        self.id = id
        self.tiempo_llenado = random.randint(1,10)
        self.tiempo_pago = 3
        self.tiempo_total = 0
        self.tiempo_llegada = 0
        self.tiempo_salida = 0

    def __str__(self):
        return "Coche " + str(self.id) + " con tiempo de llenado " + str(self.tiempo_llenado) + " y tiempo de pago " + str(self.tiempo_pago)
        
def llenar_deposito(coche):
    print("Coche " + str(coche.id) + " llega a la gasolinera")
    coche.tiempo_llegada = time.time()
    surtidor = gasolinera.asignar_surtidor()
    if surtidor == None:
        print("No hay surtidores libres")
    else:
        surtidor.ocupado = True
        print("Coche " + str(coche.id) + " se asigna el surtidor " + str(surtidor.id))
        sleep(coche.tiempo_llenado)
        surtidor.ocupado = False
        print("Coche " + str(coche.id) + " termina de llenar el deposito")
        print("Coche " + str(coche.id) + " se acerca a la caja")
        gasolinera.cola_cajas.append(coche)
        print("Coche " + str(coche.id) + " se pone en la cola de la caja")
        print("Coche " + str(coche.id) + " paga en la caja")
        sleep(coche.tiempo_pago)
        print("Coche " + str(coche.id) + " termina de pagar")
        coche.tiempo_salida = time.time()
        coche.tiempo_total = coche.tiempo_salida - coche.tiempo_llegada
        print("Coche " + str(coche.id) + " sale de la gasolinera")
        gasolinera.cola_cajas.remove(coche)
        print("Coche " + str(coche.id) + " sale de la cola de la caja")
        print('El coche ' + str(coche.id) + ' ha tardado ' + str(coche.tiempo_total) + ' segundos en llenar el deposito y pagar')

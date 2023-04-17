from multiprocessing import Pool
from time import sleep
import time
import random


#Simulamos una gasolinera con n surtidores. Cuando llega un coche, se le asigna un surtidor y se le asigna un tiempo de llenado de la gasolina.
#El tiempo de llenado de la gasolina es aleatorio y se simula con un número aleatorio entre 1 y 10.
#Tras llenar el deposito se acerca a la oficina de pago y se pone en la cola de la caja, que es única. Pago 3 minutos.
#Tras pagar retira el coche, dejando el surtidor libre aea el siguiente coche.

#Se modelarán los coches como Threads que genera el programa principal. A efectos del ejercicio se generan 50 coches.
#Realizar el problema para un tiempo T de 15 minutos y N de un surtidor de combustible
#Calcular el tiempo medio que tarda un coche desde que llega a la gasolinera hasta que sale de ella.


class Gasolinera:
    def __init__(self, n):
        self.n = n
        self.cola_cajas = []
        self.surtidores = []
        for i in range(n):
            self.surtidores.append(Surtidor(i))
      
    def asignar_surtidor(self):
        for surtidor in self.surtidores:
            if not surtidor.ocupado:
                return surtidor
        return None

    def asignar_caja(self):
        return self.cola_cajas[0]

    def __str__(self):
        return "Gasolinera con " + str(self.n) + " surtidores y " + str(len(self.cola_cajas)) + " cajas"

    
class Surtidor:
    def __init__(self, id):
        self.id = id
        self.ocupado = False

    def __str__(self):
        return "Surtidor " + str(self.id) + " " + ("ocupado" if self.ocupado else "libre")

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

if __name__ == '__main__':
    gasolinera = Gasolinera(1)
    coches = []
    for i in range(50):
        coches.append(Coche(i))
    pool = Pool(processes=50) # ESTO SIGNIFICA QUE SOLO SE PUEDEN HACER 50 PROCESOS A LA VEZ, QUE SON LOS COCHES
    pool.map(llenar_deposito, coches) # ESTO ES LO QUE HACE QUE SE EJECUTEN LOS 50 PROCESOS A LA VEZ
    print("Tiempo medio de espera: " + str(sum(coche.tiempo_total for coche in coches)/len(coches)))








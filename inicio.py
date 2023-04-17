
from multiprocessing import Pool
from time import sleep
import time
import random
from Coche import *
from Sur import *



def iniciar():
    gasolinera = Gasolinera(1)
    coches = []
    for i in range(50):
        coches.append(Coche(i))
    pool = Pool(processes=50) # ESTO SIGNIFICA QUE SOLO SE PUEDEN HACER 50 PROCESOS A LA VEZ, QUE SON LOS COCHES
    pool.map(llenar_deposito, coches) # ESTO ES LO QUE HACE QUE SE EJECUTEN LOS 50 PROCESOS A LA VEZ
    print("Tiempo medio de espera: " + str(sum(coche.tiempo_total for coche in coches)/len(coches)))

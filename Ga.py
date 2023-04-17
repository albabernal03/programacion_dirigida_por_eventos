from multiprocessing import Pool
from time import sleep
import time
import random
from Sur import *

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

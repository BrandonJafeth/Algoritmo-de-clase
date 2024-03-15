import threading
import time
import random

class Cliente(threading.Thread):
    def __init__(self, nombre, supermercado):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.supermercado = supermercado

    def run(self):
        print(f'Cliente {self.nombre} ha entrado al supermercado.')
        self.supermercado.pagar(self.nombre)

class Supermercado:
    def __init__(self, cajas):
        self.console_lock = threading.Lock()
        self.cajas = threading.Semaphore(cajas)

    def pagar(self, nombre):
        while True:
            if self.cajas._value > 2:
                self.cajas.acquire()
                self.cajas.acquire()
                print(f'{nombre} está pagando.')
                time.sleep(random.randint(1, 5))
                print(f'{nombre} ha terminado de pagar.')
                self.cajas.release()
                self.cajas.release()
                break
            else:
                with self.console_lock:
                    print(f'{nombre} está esperando para pagar.')
                time.sleep(1)


supermercado = Supermercado(5)
clientes = [Cliente(f'{i}', supermercado) for i in range(10)]

for cliente in clientes:
    cliente.start()

for cliente in clientes:
    cliente.join()

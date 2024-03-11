import threading
import time
import random

class Cliente(threading.Thread):
    def __init__(self, nombre, supermercado):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.supermercado = supermercado

    def run(self):
        self.supermercado.pagar(self.nombre)

class Supermercado:
    def __init__(self, cajas):
        self.console_lock = threading.Lock()  # Inicializa el atributo console_lock
        self.cajas = threading.Semaphore(cajas)

    def pagar(self, nombre):
        while True:
            if self.cajas._value > 2:  # Asegurarse de que al menos dos cajas registradoras permanezcan libres
                self.cajas.acquire()  # Adquirir la primera caja registradora
                self.cajas.acquire()  # Adquirir la segunda caja registradora
                print(f'{nombre} está pagando.')
                time.sleep(random.randint(1, 5))  # Simular el tiempo que tarda en pagar
                print(f'{nombre} ha terminado de pagar.')
                self.cajas.release()  # Liberar la primera caja registradora
                self.cajas.release()  # Liberar la segunda caja registradora
                break  # El cliente ha pagado, por lo que podemos salir del bucle
            else:
                with self.console_lock:
                  print(f'{nombre} está esperando para pagar.')
                time.sleep(1)  # Si no hay suficientes cajas registradoras, esperar un poco antes de intentar de nuevo
           

supermercado = Supermercado(5)  # Define the "supermercado" variable con 5 cajas registradoras disponibles
clientes = [Cliente(f'Cliente {i}', supermercado) for i in range(10)]  # 10 clientes

for cliente in clientes:
    cliente.start()

for cliente in clientes:
    cliente.join()
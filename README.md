[cola.py](https://github.com/user-attachments/files/29167658/cola.py)
class NodoTurno:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.siguiente = None

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre}"


class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    def esta_vacia(self):
        return self.head is None

    def enqueue(self, dni, nombre):
        # enqueue: O(1)
        nuevo = NodoTurno(dni, nombre)
        if self.esta_vacia():
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo

    def dequeue(self):
        # dequeue: O(1)
        if self.esta_vacia():
            return None
        atendido = self.head
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        return atendido

    def frente(self):
        # frente: O(1)
        return self.head

    def mostrar(self):
        # mostrar: O(n)
        actual = self.head
        turnos = []
        while actual:
            turnos.append(str(actual))
            actual = actual.siguiente
        return turnos


if __name__ == "__main__":
    cola = Cola()
    cola.enqueue("0102030405", "Ana")
    cola.enqueue("0999999999", "Luis")
    print("Atendido:", cola.dequeue())
    print("Frente:", cola.frente())

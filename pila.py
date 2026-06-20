class NodoAccion:
    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def push(self, accion):
        # push: O(1)
        nuevo = NodoAccion(accion)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def pop(self):
        # pop: O(1)
        if self.esta_vacia():
            return None
        accion = self.tope.accion
        self.tope = self.tope.siguiente
        return accion

    def peek(self):
        # peek: O(1)
        if self.esta_vacia():
            return None
        return self.tope.accion

    def mostrar(self):
        # mostrar: O(n)
        actual = self.tope
        acciones = []
        while actual:
            acciones.append(actual.accion)
            actual = actual.siguiente
        return acciones


if __name__ == "__main__":
    historial = Pila()
    historial.push("Registrar turno")
    historial.push("Atender cliente")
    print("Ultima accion:", historial.pop())

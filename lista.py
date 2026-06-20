class NodoCliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.siguiente = None

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre}"


class ListaClientes:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dni, nombre):
        # agregar: O(1)
        nuevo = NodoCliente(dni, nombre)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar_por_nombre(self, nombre):
        # buscar_por_nombre: O(n)
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente
        return None

    def buscar_por_dni(self, dni):
        # buscar_por_dni: O(n)
        actual = self.cabeza
        while actual:
            if actual.dni == dni:
                return actual
            actual = actual.siguiente
        return None

    def mostrar(self):
        # mostrar: O(n)
        actual = self.cabeza
        clientes = []
        while actual:
            clientes.append(str(actual))
            actual = actual.siguiente
        return clientes


if __name__ == "__main__":
    lista = ListaClientes()
    lista.agregar("0102030405", "Ana")
    lista.agregar("0999999999", "Luis")
    print("Clientes:", lista.mostrar())
    print("Buscar Ana:", lista.buscar_por_nombre("Ana"))

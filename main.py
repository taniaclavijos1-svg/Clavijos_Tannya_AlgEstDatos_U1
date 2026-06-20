from pila import Pila
from cola import Cola
from lista import ListaClientes


def mostrar_menu():
    print("\n===== Gestor de turnos CarUPS =====")
    print("1. Registrar cliente y turno")
    print("2. Atender siguiente cliente")
    print("3. Buscar cliente por nombre")
    print("4. Mostrar clientes registrados")
    print("5. Mostrar cola de turnos")
    print("6. Mostrar historial de acciones")
    print("7. Deshacer ultima accion")
    print("0. Salir")


def registrar_cliente(lista_clientes, cola_turnos, historial):
    dni = input("Ingrese DNI del cliente: ").strip()
    nombre = input("Ingrese nombre del cliente: ").strip()

    if not dni or not nombre:
        print("DNI y nombre son obligatorios.")
        return

    lista_clientes.agregar(dni, nombre)  # agregar: O(1)
    cola_turnos.enqueue(dni, nombre)     # enqueue: O(1)
    historial.push(f"Registrar turno: {dni} - {nombre}")  # push: O(1)
    print("Cliente registrado y turno agregado correctamente.")


def atender_cliente(cola_turnos, historial):
    atendido = cola_turnos.dequeue()  # dequeue: O(1)
    if atendido is None:
        print("No hay turnos pendientes.")
    else:
        historial.push(f"Atender cliente: {atendido.dni} - {atendido.nombre}")  # push: O(1)
        print(f"Cliente atendido: {atendido}")


def buscar_cliente(lista_clientes):
    nombre = input("Ingrese el nombre a buscar: ").strip()
    cliente = lista_clientes.buscar_por_nombre(nombre)  # buscar_por_nombre: O(n)
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente no encontrado.")


def mostrar_lista(titulo, elementos):
    print(f"\n--- {titulo} ---")
    if not elementos:
        print("No existen registros.")
    else:
        for item in elementos:
            print(item)


def deshacer(historial):
    accion = historial.pop()  # pop: O(1)
    if accion is None:
        print("No hay acciones para deshacer.")
    else:
        print(f"Se deshizo la accion: {accion}")
        print("Nota: para esta actividad se deshace el registro del historial; no se revierten datos ya almacenados.")


def casos_de_prueba():
    print("\nEjecutando casos de prueba...")
    pila = Pila()
    pila.push("Prueba pila")
    assert pila.pop() == "Prueba pila"

    cola = Cola()
    cola.enqueue("111", "Cliente Cola")
    assert cola.dequeue().nombre == "Cliente Cola"

    lista = ListaClientes()
    lista.agregar("222", "Cliente Lista")
    assert lista.buscar_por_nombre("Cliente Lista").dni == "222"
    print("Casos de prueba correctos: pila, cola y lista enlazada funcionan.")


def main():
    lista_clientes = ListaClientes()
    cola_turnos = Cola()
    historial = Pila()

    casos_de_prueba()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_cliente(lista_clientes, cola_turnos, historial)
        elif opcion == "2":
            atender_cliente(cola_turnos, historial)
        elif opcion == "3":
            buscar_cliente(lista_clientes)
        elif opcion == "4":
            mostrar_lista("Clientes registrados", lista_clientes.mostrar())
        elif opcion == "5":
            mostrar_lista("Cola de turnos", cola_turnos.mostrar())
        elif opcion == "6":
            mostrar_lista("Historial de acciones", historial.mostrar())
        elif opcion == "7":
            deshacer(historial)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()

# Gestor de turnos CarUPS - Unidad 1

Repositorio sugerido: `Clavijos_Tania_AlgEstDatos_U1`

## Descripcion

Este proyecto implementa un programa de consola en Python para gestionar los turnos de atencion del taller CarUPS. Integra tres estructuras de datos lineales vistas en la Unidad 1:

- Pila para el historial de acciones.
- Cola para los turnos de atencion.
- Lista simplemente enlazada para los clientes registrados.

Las estructuras fueron implementadas desde nodos propios, sin usar listas de Python como estructura principal.

## Archivos

- `pila.py`: implementa la pila mediante nodos.
- `cola.py`: implementa la cola mediante nodos con referencias `head` y `tail`.
- `lista.py`: implementa la lista simplemente enlazada de clientes.
- `main.py`: integra las estructuras mediante un menu de consola.

## Como ejecutar

1. Tener instalado Python 3.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

## Estructuras utilizadas

### Pila

La pila registra las acciones del operador, como registrar un turno o atender un cliente. Es adecuada porque usa el principio LIFO, donde la ultima accion realizada es la primera que se puede deshacer.

### Cola

La cola gestiona los turnos de atencion. Es adecuada porque usa el principio FIFO, donde el primer cliente en llegar es el primero en ser atendido.

### Lista enlazada

La lista simplemente enlazada mantiene los clientes registrados. Permite agregar clientes, buscar por nombre y mostrar todos los clientes mediante recorrido desde la cabeza.

## Tabla de complejidades

| Estructura | Operacion | Complejidad | Justificacion |
|---|---:|---:|---|
| Pila | push | O(1) | Inserta en el tope sin recorrer nodos. |
| Pila | pop | O(1) | Elimina el nodo del tope directamente. |
| Pila | peek | O(1) | Consulta el tope directamente. |
| Pila | mostrar | O(n) | Recorre todos los nodos del historial. |
| Cola | enqueue | O(1) | Inserta al final usando la referencia `tail`. |
| Cola | dequeue | O(1) | Elimina el frente usando la referencia `head`. |
| Cola | frente | O(1) | Consulta el primer nodo directamente. |
| Cola | mostrar | O(n) | Recorre todos los turnos. |
| Lista enlazada | agregar | O(1) | Inserta al inicio de la lista. |
| Lista enlazada | buscar por nombre | O(n) | Puede requerir recorrer todos los nodos. |
| Lista enlazada | buscar por DNI | O(n) | Puede requerir recorrer todos los nodos. |
| Lista enlazada | mostrar | O(n) | Recorre todos los clientes registrados. |

## Casos de prueba

El archivo `main.py` ejecuta al inicio un caso de prueba por estructura:

- Pila: inserta y elimina una accion.
- Cola: inserta y atiende un cliente.
- Lista enlazada: registra y busca un cliente.

## Bibliografia

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). *Data Structures and Algorithms in Java*. Wiley.

Weiss, M. A. (2011). *Data Structures and Algorithm Analysis in Java* (3rd ed.). Pearson.

#----Importaciones-------------------------------------------------------------------------------------------------------------------------------------------
import os
import platform
#----Funciones----------------------------------------------------------------------------------------------------------------------------------------------
def limpiar():

    varClear = "Clear"
    if platform.system() == "Windows":
        varClear = "cls"

    else:
        varClear = "clear"

    os.system(varClear)

def enter():

    input("\npresiona ENTER para continuar\n")
    limpiar()

def invalido():

    print("Ijoles, creo que tu opcion no es valida chavo.")
#-----------------------------------------------------------------------------Tareas-------------------------------------------------------------------------------
class Subtarea:
    def __init__(self, nombre, estado="Pendiente"):

        self.nombre = nombre
        self.estado = estado

    def __str__(self):

        return f"Subtarea: {self.nombre}, Estado: {self.estado}"

class Tarea:
    def __init__(self, nombre):

        self.nombre = nombre
        self.subtareas = []

    def agregarSubtarea(self, nombreSubtarea):

        nuevaSubtarea = Subtarea(nombreSubtarea)
        self.subtareas.append(nuevaSubtarea)
        print(f"Subtarea '{nombreSubtarea}' agregada a la tarea '{self.nombre}'.")

    def listarSubtareas(self):
        if not self.subtareas:
            print(f"No hay subtareas para la tarea '{self.nombre}'.")

        else:
            print(f"Subtareas de '{self.nombre}':")
            for idx, subtarea in enumerate(self.subtareas, start=1):
                print(f"{idx}. {subtarea}")

    def actualizarSubtarea(self, indice, nuevoEstado):

        if 0 <= indice < len(self.subtareas):
            self.subtareas[indice].estado = nuevoEstado

            print(f"Subtarea '{self.subtareas[indice].nombre}' actualizada a '{nuevoEstado}'.")
        else:
            print("Índice de subtarea no valido.")

    def __str__(self):
        return f"Tarea: {self.nombre}"


ListaTareas = []

def crearTarea():
    nombreTarea = input("Ingrese el nombre de la tarea: ")
    nuevaTarea = Tarea(nombreTarea)
    ListaTareas.append(nuevaTarea)
    print(f"Tarea '{nombreTarea}' creada con exito.")

def listarTareas():
    if not ListaTareas:
        print("No hay tareas registradas.")
    else:
        print("\nLista de Tareas:")
        for idx, tarea in enumerate(ListaTareas, start=1):
            print(f"{idx}. {tarea}")

def gestionarSubtareas():

    listarTareas()
    if ListaTareas:
        indiceTarea = int(input("Seleccione el número de la tarea para gestionar subtareas: ")) - 1
        if 0 <= indiceTarea < len(ListaTareas):
            tareaSeleccionada = ListaTareas[indiceTarea]
            while True:

                enter()

                print(f"\nGestionando subtareas de '{tareaSeleccionada.nombre}'")
                print("\n\t1. Agregar Subtarea")
                print("\t2. Listar Subtareas")
                print("\t3. Actualizar Subtarea")
                print("\t4. Volver al menú principal")
                opcion = input("\nSeleccione una opción: ")

                enter()

                if opcion == '1':
                    nombreSubtarea = input("Ingrese el nombre de la subtarea: ")
                    tareaSeleccionada.agregarSubtarea(nombreSubtarea)

                elif opcion == '2':
                    tareaSeleccionada.listarSubtareas()

                elif opcion == '3':
                    tareaSeleccionada.listarSubtareas()
                    indiceSubtarea = int(input("Seleccione el número de la subtarea a actualizar: ")) - 1
                    nuevoEstado = input("Ingrese el nuevo estado de la subtarea: ")
                    tareaSeleccionada.actualizarSubtarea(indiceSubtarea, nuevoEstado)

                elif opcion == '4':
                    break

                else:
                    invalido()
        else:
            invalido()

def gestionTareas():
    while True:
        enter()

        print("\nGestion de Tareas")
        print("\n\t1. Crear Tarea")
        print("\t2. Mostrar Tareas")
        print("\t3. Gestionar Subtareas")
        print("\t4. Regresar al menu principal")
        opcion = input("\nSeleccione una opcion: ")

        enter()

        if opcion == '1':
            crearTarea()

        elif opcion == '2':
            listarTareas()

        elif opcion == '3':
            gestionarSubtareas()

        elif opcion == '4':
            break
        else:
            invalido()

#------------------------------------------------------------------------Producto------------------------------------------------------------------------

class Producto:
    def __init__(self, nombre, descripcion, idProducto, cantidad):

        self.nombre = nombre
        self.descripcion = descripcion
        self.idProducto = idProducto
        self.cantidad = int(cantidad)

    def __str__(self):
        return f"Producto(ID: {self.idProducto}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad})"


ListaProductos = []

def registrarProducto():

    nombreProducto = input("Ingrese el nombre del producto: ")
    descripcionProducto = input("Describa el producto: ")
    idProducto = input("Ingrese el código de barras: ")
    cantidadProducto = input("¿Cuántos son?: ")
    nuevoProducto = Producto(nombreProducto, descripcionProducto, idProducto, cantidadProducto)
    ListaProductos.append(nuevoProducto)

    print("Producto registrado con exito.")

def eliminarProducto():
    idProducto = input("Ingrese el ID del producto a eliminar: ")
    for producto in ListaProductos:

        if producto.idProducto == idProducto:

            ListaProductos.remove(producto)
            print(f"Producto {producto.nombre} eliminado con exito.")
            return
        
    print("Producto no encontrado.")

def editarProducto():
    idProducto = input("Ingrese el ID del producto a editar: ")
    for producto in ListaProductos:
        if producto.idProducto == idProducto:

            print("Producto encontrado\nQue deseas editar?.")
            print("\n\t1. Nombre")
            print("\t2. Descripcion")
            print("\t3. Cantidad")

            opcion = input("\nSeleccione una opcion: ")

            if opcion == '1':
                nuevoNombre = input("Ingrese el nuevo nombre: ")
                producto.nombre = nuevoNombre

            elif opcion == '2':
                nuevaDescripcion = input("Ingrese la nueva descripcion: ")
                producto.descripcion = nuevaDescripcion

            elif opcion == '3':
                nuevaCantidad = input("Ingrese la nueva cantidad: ")
                producto.cantidad = int(nuevaCantidad)

            print("Producto actualizado con exito.")

            return
    print("Producto no encontrado.")

def listarProductos():
    if not ListaProductos:
        print("No hay productos registrados.")
    else:
        print("\nLista de Productos:")
        for producto in ListaProductos:
            print(producto)

def gestionProductos():
    while True:
        enter()

        print("\nGestion de Productos")
        print("\n\t1. Registrar Producto")
        print("\t2. Editar Producto")
        print("\t3. Eliminar Producto")
        print("\t4. Mostrar Productos")
        print("\t5. Regresar")

        opcion = input("\nSeleccione una opcion: ")
        enter()

        if opcion == '1':
            registrarProducto()

        elif opcion == '2':
            editarProducto()

        elif opcion == '3':
            eliminarProducto()

        elif opcion == '4':
            listarProductos()

        elif opcion == '5':
            break
        else:
            invalido()

#-------------------------------------------------Gestion grupal----------------------------------------------------------------------------------------------

class Estudiante:
    def __init__(self, nombre, idEstudiante):
        self.nombre = nombre
        self.idEstudiante = idEstudiante
        self.calificaciones = {}

    def agregarCalificacion(self, materia, calificacion):
        self.calificaciones[materia] = calificacion
        print(f"Calificación {calificacion} agregada en {materia} para {self.nombre}.")

    def listarCalificaciones(self):
        print(f"Calificaciones de {self.nombre}:")
        for materia, calificacion in self.calificaciones.items():
            print(f"\t{materia}: {calificacion}")

    def __str__(self):
        return f"Estudiante(ID: {self.idEstudiante}, Nombre: {self.nombre})"

ListaEstudiantes = []

def registrarEstudiante():
    nombreEstudiante = input("Ingrese el nombre del estudiante: ")
    idEstudiante = input("Ingrese el ID del estudiante: ")
    nuevoEstudiante = Estudiante(nombreEstudiante, idEstudiante)
    ListaEstudiantes.append(nuevoEstudiante)
    print(f"Estudiante '{nombreEstudiante}' registrado con exito.")

def editarEstudiante():
    idEstudiante = input("Ingrese el ID del estudiante a editar: ")
    for estudiante in ListaEstudiantes:
        if estudiante.idEstudiante == idEstudiante:
            print("Estudiante encontrado.")
            nuevoNombre = input("Ingrese el nuevo nombre: ")
            estudiante.nombre = nuevoNombre
            print("Nombre del estudiante actualizado con exito.")
            return
    print("Estudiante no encontrado.")

def agregarCalificacion():
    idEstudiante = input("Ingrese el ID del estudiante: ")
    for estudiante in ListaEstudiantes:
        if estudiante.idEstudiante == idEstudiante:
            materia = input("Ingrese la materia: ")
            calificacion = input("Ingrese la calificacion: ")
            estudiante.agregarCalificacion(materia, calificacion)
            return
    print("Estudiante no encontrado.")

def listarEstudiantes():
    if not ListaEstudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\nLista de Estudiantes:")
        for estudiante in ListaEstudiantes:
            print(estudiante)

def listarCalificaciones():
    idEstudiante = input("Ingrese el ID del estudiante: ")
    for estudiante in ListaEstudiantes:
        if estudiante.idEstudiante == idEstudiante:
            estudiante.listarCalificaciones()
            return
    print("Estudiante no encontrado.")

def gestionGrupos():
    while True:
        enter()
        print("\nGestion de Estudiantes")
        print("\n\t1. Registrar Estudiante")
        print("\t2. Editar Estudiante")
        print("\t3. Agregar Calificacion")
        print("\t4. Mostrar Estudiantes")
        print("\t5. Mostrar Calificaciones de un Estudiante")
        print("\t6. Regresar")

        opcion = input("\nSeleccione una opcion: ")
        enter()

        if opcion == '1':
            registrarEstudiante()
        elif opcion == '2':
            editarEstudiante()
        elif opcion == '3':
            agregarCalificacion()
        elif opcion == '4':
            listarEstudiantes()
        elif opcion == '5':
            listarCalificaciones()
        elif opcion == '6':
            break
        else:
            invalido()

def menu():
    while True:
        enter()
        print("\nSeleccione una opcion:")
        print("\n\t1. Gestion de inventario")
        print("\t2. Gestion de tareas")
        print("\t3. Gestion grupal")
        print("\t0. Salir")

        opcion = int(input("\n\tIngrese el numero de la opcion: "))
        enter()
        if opcion == 1:
            gestionProductos()
        elif opcion == 2:
            gestionTareas()
        elif opcion == 3:
            gestionGrupos()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            invalido()
#---- Programa Principal------------------------------------------------------------------------------------------------------------------------------------
menu()
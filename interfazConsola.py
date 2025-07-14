import os
import pandas as pd
from dotenv import load_dotenv
import consultas
load_dotenv()

def iniciarAplicacion():
    print("\n" + "=" * 50)
    print(" 🛠️ BIENVENIDO AL SISTEMA DE GESTION DE REPUESTOS ".center(50, '='))
    print("=" * 50)
    print("¿Que deseas hacer?")
    print("=" * 50)
    print("\n1. Generar excel personalizado")
    print("2. Administrar excel")
    print("\n" + "=" * 50)
    print("3. Salir")

pathPrecioRepuestos= os.getenv("PATH_PRECIO_REPUESTOS")
pathCatalogoRepuestos= os.getenv("PATH_CATALOGO_RESPUESTOS")
pathStockRepuestos = os.getenv("PATH_STOCK_REPUESTOS")

def main():
    while True:
        iniciarAplicacion()
        opcion = input("\nSeleccione una opción (1-3): ")
        if opcion == "1":
            interfazConsultaPerzonalizada()
        elif opcion == "2":
            administrarExcel()
        elif opcion == "3":
            print("\n¡Hasta pronto! 👋\n")
            break
def interfazConsultaPerzonalizada():
    print("entre al primero")
def administrarExcel():
    while True:
        print("\n" + "=" * 50)
        print(" 📁 ADMINISTRAR EXCEL ".center(50, '='))
        print("=" * 50)
        print("\n1. Consultar datos")
        print("2. Añadir datos")
        print("3. Actualizar datos")
        print("4. Eliminar datos")
        print("5. Volver al menú principal")
        print("\n" + "=" * 50)

        opcion_CRUD = input("\nSeleccione una opción (1-5): ")

        if opcion_CRUD == "5":
            break

        if opcion_CRUD in ["1", "2", "3", "4"]:
            while True:
                print("\n" + "=" * 50)
                print(" 📁 ESCOGER EL EXCEL ".center(50, '='))
                print("=" * 50)
                print("\n1. Precio Stock Repuestos")
                print("2. Stock Repuestos")
                print("3. Catalogo Repuestos")
                print("4. Volver al menú anterior")
                print("\n" + "=" * 50)

                opcion_excel = input("\nSeleccione un archivo (1-4): ")

                if opcion_excel == "4":
                    break
                elif opcion_excel in ["1", "2", "3"]:
                    escogerAccionBaseOnExcel(opcion_excel,opcion_CRUD)
                    break
                else:
                    print("\n❌ Opción no válida. Por favor ingrese 1-4")
        else:
            print("\n❌ Opción no válida. Por favor ingrese 1-5")
def escogerAccionBaseOnExcel(opcionExcel,opcionCRUD):
    if opcionExcel == "1":
        accionesCRUDPrecioStockRepuestos(opcionCRUD)
    elif opcionExcel == "2":
        accionesCRUDStockRepuestos(opcionCRUD)
    elif opcionExcel == "3":
        accionesCRUDCatalogoRepuestos(opcionCRUD)

def consultarDatosInterfazGeneral(archivo, nameExcel):
    print("\n" + "=" * 50)
    print(" 📁 CONSULTA DE DATOS - "+nameExcel.center(50, '='))
    print("=" * 50)
    id = input("\nEscriba el id: ")
    if archivo == pathPrecioRepuestos:
        consultas.consultar_datos(int(id),'ID_MATERIAL',pathPrecioRepuestos)
    elif archivo == pathCatalogoRepuestos:
        consultas.consultar_datos(int(id),'ID_MATERIAL',pathCatalogoRepuestos)
    elif archivo == pathStockRepuestos:
        consultas.consultar_datos(int(id),'ID_MATERIAL',pathStockRepuestos)
def eliminarDatosInterfazGeneral(archivo,nameExcel):
    print("\n" + "=" * 50)
    print(" 📁 ELIMINAR DATOS - "+nameExcel.center(50, '='))
    print("=" * 50)
    id = input("\nEscriba el id: ")
    if archivo == pathPrecioRepuestos:
        consultas.eliminar_datos(int(id),'ID_MATERIAL',pathPrecioRepuestos)
    elif archivo == pathCatalogoRepuestos:
        consultas.eliminar_datos(int(id),'ID_MATERIAL',pathCatalogoRepuestos)
    elif archivo == pathStockRepuestos:
        consultas.eliminar_datos(int(id),'ID_MATERIAL',pathStockRepuestos)
def ingresarItemPrecioStockRepuestos(archivo,nameExcel):
    print("\n" + "=" * 50)
    print(" 📁 INSERTAR DATOS A "+nameExcel.center(50, '='))
    print("=" * 50)
    precio = input("\nEscriba el precio: ")
    nuevos_datos = pd.DataFrame([[consultas.obtenerID('ID_MATERIAL',archivo), float(precio)]],columns=['ID_MATERIAL','PRECIO'])
    consultas.insertar_datos(nuevos_datos,archivo)
    print("==========SE INGRESO CORRECTAMETE LOS DATOS")
def ingresarItemStockRepuestos(archivo,nameExcel):
    print("\n" + "=" * 50)
    print(" 📁 INSERTAR DATOS A "+nameExcel.center(50, '='))
    print("=" * 50)
    material = input("\nEscriba material: ")
    stock = input("\nEscriba el stock: ")
    unidad = input("\nEscriba la unidad: ")
    nuevos_datos = pd.DataFrame([[consultas.obtenerID('ID_MATERIAL',archivo), material,int(stock),unidad]],columns=['ID_MATERIAL','TEXTO_MATERIAL','STOCK','UNIDAD'])
    consultas.insertar_datos(nuevos_datos,archivo)
    print("==========SE INGRESO CORRECTAMETE LOS DATOS")
def ingresarItemCatalogoRepuestos(archivo,nameExcel):
    print("\n" + "=" * 50)
    print(" 📁 INSERTAR DATOS A " + nameExcel.center(50, '='))
    print("=" * 50)
    descripcionMaterial = input("\nEscriba el precio: ")
    proveedorMaterial = input("\nEscriba el proveedor del material: ")
    numeroProveedor = input("\nEscriba el numero de proveedor: ")
    fabricante = input("\nEscriba el fabricante componente: ")
    numeroFabricante = input("\nEscriba el numero de fabricante: ")
    ubicacion =  input("\nEscriba la ubicacion: ")
    nuevos_datos =  pd.DataFrame([[consultas.obtenerID('ID_MATERIAL',archivo), descripcionMaterial,proveedorMaterial,numeroProveedor,fabricante,numeroFabricante,ubicacion]],columns=['ID_MATERIAL','DESCRIPCION_MATERIAL','PROVEEDOR_MATERIAL','NP_PROVEEDOR','FABRICANTE_COMPONENTE','NP_FABRICANTE','UBICACION'])
    consultas.insertar_datos(nuevos_datos, archivo)
    print("==========SE INGRESO CORRECTAMETE LOS DATOS")
'''
def actualizarItemPrecioStockRepuestos(archivo,nameExcel):
def actualizarItemStockRepuestos(archivo,nameExcel):
def actualizarItemCatalogoRepuestos(archivo,nameExcel):
'''


def accionesCRUDPrecioStockRepuestos(opcionCRUD):
    if opcionCRUD == "1":
        consultarDatosInterfazGeneral(pathPrecioRepuestos, "PRECIO STOCK DE REPUESTOS")
    elif opcionCRUD == "2":
        ingresarItemPrecioStockRepuestos(pathPrecioRepuestos, "PRECIO STOCK DE REPUESTOS")
    elif opcionCRUD == "4":
        eliminarDatosInterfazGeneral(pathPrecioRepuestos,"PRECIO STOCK DE REPUESTOS")

def accionesCRUDStockRepuestos(opcionCRUD):
    if opcionCRUD == "1":
        consultarDatosInterfazGeneral(pathStockRepuestos,"STOCK DE REPUESTOS")
    elif opcionCRUD == "2":
        ingresarItemStockRepuestos(pathPrecioRepuestos, "STOCK DE REPUESTOS")
    elif opcionCRUD == "4":
        eliminarDatosInterfazGeneral(pathStockRepuestos,"STOCK DE REPUESTOS")

def accionesCRUDCatalogoRepuestos(opcionCRUD):
    if opcionCRUD == "1":
        consultarDatosInterfazGeneral(pathCatalogoRepuestos,"CATALOGO DE REPUESTOS")
    elif opcionCRUD == "2":
        ingresarItemCatalogoRepuestos(pathPrecioRepuestos, "CATALOGO DE REPUESTOS")
    elif opcionCRUD == "4":
        eliminarDatosInterfazGeneral(pathCatalogoRepuestos,"CATALOGO DE REPUESTOS")



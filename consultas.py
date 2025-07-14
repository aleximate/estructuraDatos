import pandas as pd


def obtenerID(columna, archivo):
    datos = pd.read_excel(archivo)
    ultimo_id = datos[columna].iloc[-1]
    return int(ultimo_id) + 1

#Funcion para insertar datos al excel
def insertar_datos(datos_nuevos, archivo):
    datos_existentes = pd.read_excel(archivo)
    datos_completos = pd.concat([datos_existentes, datos_nuevos], ignore_index=True)
    datos_completos.to_excel(archivo, index=False)

#Funcion para eliminar datos al excel
def eliminar_datos(valor, columna, archivo):
    datos = pd.read_excel(archivo)
    datos_actualizados = datos[datos[columna] != valor]
    datos_actualizados.to_excel(archivo, index=False)
    return datos_actualizados

#Funcion para actualizar datos al excel
def actualizar_datos(id_buscar, columna, nuevos_valores, archivo):
    datos = pd.read_excel(archivo)
    mask = datos[columna] == id_buscar
    for columnas, valor in nuevos_valores.items():
        if columnas in datos.columns and columnas != columna:
            datos.loc[mask, columnas] = valor

    datos.to_excel(archivo, index=False)
    return datos


def consultar_datos(id_buscar, columna, archivo):
    datos = pd.read_excel(archivo)
    registro = datos[datos[columna] == id_buscar]

    if registro.empty:
        print(f"\n⚠️ No se encontró el ID {id_buscar} en la columna {columna}")
        return None
    print("\n" + "=" * 50)
    print(f"📋 REGISTRO ENCONTRADO - ID: {id_buscar}")
    print("=" * 50)
    for col, val in registro.iloc[0].items():
        print(f"{col}: {val}")
    print("=" * 50 + "\n")

    return registro.iloc[0]

'''
nuevos_datos = pd.DataFrame([[obtenerID('ID_MATERIAL',pathPrecioRepuestos), 150.50]], columns=['ID_MATERIAL', 'PRECIO'])
insertar_datos(nuevos_datos, pathPrecioRepuestos)
eliminar_datos(807562,'ID_MATERIAL',pathPrecioRepuestos)
actualizar_datos(
    id_buscar= 100012,
    columna= 'ID_MATERIAL',
    nuevos_valores={'PRECIO': 666.00},
    archivo=pathPrecioRepuestos
)
consultar_datos(
    id_buscar= 100023,
    columna='ID_MATERIAL',
    archivo= pathPrecioRepuestos
)
'''



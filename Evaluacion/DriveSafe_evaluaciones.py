import json
import os

RUTA_ARCHIVO = "./evaluaciones.json"

def cargar_datos_evaluaciones():




    if os.path.exists(RUTA_ARCHIVO) and os.path.getsize(RUTA_ARCHIVO) > 0:
        try:
            with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                
                if "evaluaciones" not in datos:
                    datos["evaluaciones"] = {}
                return datos
        except Exception:
            
            return {"evaluaciones": {}}
    else:
        
        return {"evaluaciones": {}}

def guardar_datos(evaluaciones):
    
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(evaluaciones, archivo, indent=4, ensure_ascii=False)

def crear_evaluacion(datos):
    
    print("\n--- Registrar Nueva Evaluación ---")
    id_evaluacion = input("Ingrese el documento o ID del evaluado: ").strip()
    
    if not id_evaluacion:
        print("Error: El ID no puede estar vacío.")
        return

    nombre = input("Ingrese el nombre completo del evaluado: ").strip()
    nota = input("Ingrese la nota o resultado (Por ejemplo: 85 o Aprobado): ").strip()
    observaciones = input("Ingrese las observaciones: ").strip()
    


    datos["evaluaciones"][id_evaluacion] = {
        "nombre": nombre,
        "nota": nota,
        "observaciones": observaciones
    }
    

    guardar_datos(datos)
    print("Evaluación registrada correctamente")



def listar_evaluaciones(datos):
    print("\n--- Lista de Evaluaciones ---")
    evaluaciones = datos.get("evaluaciones", {})
    
    if not evaluaciones:
        print("No hay evaluaciones registradas actualmente.")
        return

    for id_eval, info in evaluaciones.items():
        print(f"\nDocumento: {id_eval}")
        print(f"  Nombre: {info.get('nombre', 'Sim nombre')}")
        print(f"  Nota/Resultado: {info.get('nota', 'Sin nota')}")
        print(f"  Observaciones: {info.get('observaciones', 'Sin observaciones')}")


def menu_evaluados():

    evaluaciones = cargar_datos_evaluaciones()
    
    while True:
        print("\n--- Menú Principal DriveSafe ---")
        print("1. Nueva evaluacion")
        print("2. Listar evaluaciones")
        print("3. Volver al menú")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            crear_evaluacion(evaluaciones)
        elif opcion == "2":
            listar_evaluaciones(evaluaciones)
        elif opcion == "3":
            print("Volviendo al menú...")
            return 
        elif opcion == "4":
            return
        else:
            print("Error, opción no disponible, intenta de nuevo.")
    
    
if __name__ == "__main__":
    menu_evaluados()

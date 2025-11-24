import random
import math
import time
import itertools

# Constantes
LETRAS_MAYUSCULAS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
LETRAS_MINUSCULAS = "abcdefghijklmnñopqrstuvwxyz"
NUMEROS = "0123456789"
SIMBOLOS = ".,-_!@#$%&*()[]{}<>?/|"
CARACTERES_POSIBLES = LETRAS_MAYUSCULAS + LETRAS_MINUSCULAS + NUMEROS + SIMBOLOS
INTENTOS_POR_SEGUNDO = 1e6  # Adaptado para hardware común de oficina (~1 millón de intentos/seg en CPU estándar)

def estimar_fuerza_contrasena(contrasena):
    longitud = len(contrasena)
    if longitud == 0:
        return {"error": "La contraseña no puede estar vacía."}
    
    # Verificar tipos de caracteres
    tiene_mayus = any(c in LETRAS_MAYUSCULAS for c in contrasena)
    tiene_minus = any(c in LETRAS_MINUSCULAS for c in contrasena)
    tiene_numeros = any(c in NUMEROS for c in contrasena)
    tiene_simbolos = any(c in SIMBOLOS for c in contrasena)
    
    # Calcular tamaño efectivo
    tamano_efectivo = sum([
        len(LETRAS_MINUSCULAS) if tiene_minus else 0,
        len(LETRAS_MAYUSCULAS) if tiene_mayus else 0,
        len(NUMEROS) if tiene_numeros else 0,
        len(SIMBOLOS) if tiene_simbolos else 0
    ]) or len(LETRAS_MINUSCULAS)
    
    # Evitar overflow: usar log para combinaciones grandes
    if longitud > 100:
        combinaciones = float('inf')
        entropia = float('inf')
    else:
        combinaciones = tamano_efectivo ** longitud
        entropia = math.log2(combinaciones) if combinaciones > 0 else 0
    
    # Estimación de tiempo
    tiempo_segundos = combinaciones / INTENTOS_POR_SEGUNDO if combinaciones != float('inf') else float('inf')
    tiempo_dias = tiempo_segundos / (60 * 60 * 24) if tiempo_segundos != float('inf') else float('inf')
    tiempo_meses = tiempo_dias / 30 if tiempo_dias != float('inf') and tiempo_dias > 30 else 0
    tiempo_anos = tiempo_meses // 12 if tiempo_meses > 12 else 0
    
    # Clasificación
    if entropia < 28:
        clasificacion = "Muy débil"
    elif entropia < 36:
        clasificacion = "Débil"
    elif entropia < 60:
        clasificacion = "Moderada"
    elif entropia < 128:
        clasificacion = "Fuerte"
    else:
        clasificacion = "Muy fuerte"
    
    return {
        "longitud": longitud,
        "tamano_conjunto": tamano_efectivo,
        "combinaciones": combinaciones,
        "entropia_bits": entropia,
        "clasificacion": clasificacion,
        "tiempo_estimado_segundos": tiempo_segundos,
        "tiempo_estimado_dias": tiempo_dias,
        "tiempo_estimado_meses": tiempo_meses,
        "tiempo_estimado_anos": tiempo_anos
    }

# Pedir contraseña
try:
    contrasena = input("Ingresa tu contraseña para verificar su seguridad: ").strip()
except KeyboardInterrupt:
    print("\nSaliendo...")
    exit()

# Validar caracteres
if not all(c in CARACTERES_POSIBLES for c in contrasena):
    print("Error: La contraseña contiene caracteres no soportados.")
    exit()

# Menú
print("\nElige una opción:")
print("1. Verificación exhaustiva ordenada (prueba todas las combinaciones en orden, por longitud creciente)")
print("2. Verificación inteligente (construye la contraseña carácter por carácter)")
print("3. Mostrar análisis detallado de la contraseña")
try:
    opcion = input("Ingresa 1, 2 o 3: ").strip()
except KeyboardInterrupt:
    print("\nSaliendo...")
    exit()

if opcion == "1":
    print("\nIniciando verificación exhaustiva ordenada...")
    print("Nota: Se mostrarán actualizaciones cada 10,000 intentos. Para contraseñas de 4-8 caracteres, puede tardar tiempo en hardware común.")
    
    contador = 0
    encontrada = False
    longitud_contrasena = len(contrasena)
    
    for longitud_actual in range(1, longitud_contrasena + 1):
        print(f"\nProbando combinaciones de longitud {longitud_actual}...")
        for combinacion in itertools.product(CARACTERES_POSIBLES, repeat=longitud_actual):
            attempt = ''.join(combinacion)
            contador += 1
            
            if contador % 10000 == 0:
                print(f"Intentos: {contador}, probando: {attempt}")
            
            if attempt == contrasena:
                print(f"\n¡Encontrada en {contador} intentos! Contraseña: {attempt}")
                encontrada = True
                break
        
        if encontrada:
            break
    
    if not encontrada:
        print(f"No encontrada en {contador} intentos. Probablemente fuerte.")

elif opcion == "2":
    print("\nIniciando verificación inteligente...")
    print("Nota: Se mostrarán intentos por posición.")
    
    contador = 0
    contrasena_descifrada = ""
    
    for i in range(len(contrasena)):
        print(f"\nBuscando carácter en posición {i+1}...")
        for char in CARACTERES_POSIBLES:
            attempt = contrasena_descifrada + char + "?" * (len(contrasena) - i - 1)
            contador += 1
            print(f"Intento {contador}: Probando '{attempt}'")
            
            if char == contrasena[i]:
                contrasena_descifrada += char
                print(f"¡Encontrado! Parcial: '{contrasena_descifrada}'")
                break
    
    print(f"\n¡Completada en {contador} intentos!")

elif opcion == "3":
    # Mostrar análisis detallado
    resultado = estimar_fuerza_contrasena(contrasena)
    if "error" in resultado:
        print(resultado["error"])
    else:
        print(f"\nAnálisis detallado de '{contrasena}':")
        print(f"Longitud: {resultado['longitud']}")
        print(f"Conjunto usado: {resultado['tamano_conjunto']} caracteres")
        print(f"Combinaciones posibles: {int(resultado['combinaciones'])}" if resultado['combinaciones'] != float('inf') else "Combinaciones posibles: Infinito")
        print(f"Entropía: {resultado['entropia_bits']:.2f} bits")
        print(f"Clasificación: {resultado['clasificacion']}")
        if resultado['tiempo_estimado_segundos'] != float('inf'):
            print(f"Tiempo estimado de crackeo: {int(resultado['tiempo_estimado_segundos'])} segundos, {int(resultado['tiempo_estimado_dias'])} días, {int(resultado['tiempo_estimado_meses'])} meses, {int(resultado['tiempo_estimado_anos'])} años")
        else:
            print("Tiempo estimado de crackeo: Infinito (muy fuerte)")

else:
    print("Opción inválida.")
    exit()

# Mostrar análisis al final para opciones 1 y 2
if opcion in ["1", "2"]:
    resultado = estimar_fuerza_contrasena(contrasena)
    if "error" not in resultado:
        print(f"\nAnálisis de '{contrasena}':")
        print(f"Longitud: {resultado['longitud']}")
        print(f"Conjunto usado: {resultado['tamano_conjunto']} caracteres")
        print(f"Combinaciones posibles: {int(resultado['combinaciones'])}" if resultado['combinaciones'] != float('inf') else "Combinaciones posibles: Infinito")
        print(f"Entropía: {resultado['entropia_bits']:.2f} bits")
        print(f"Clasificación: {resultado['clasificacion']}")
        if resultado['tiempo_estimado_segundos'] != float('inf'):
            print(f"Tiempo estimado de crackeo: {int(resultado['tiempo_estimado_segundos'])} segundos, {int(resultado['tiempo_estimado_dias'])} días, {int(resultado['tiempo_estimado_meses'])} meses, {int(resultado['tiempo_estimado_anos'])} años")
        else:
            print("Tiempo estimado de crackeo: Infinito (muy fuerte)")

print("\nRecuerda: Educativo. Usa hashing en la práctica.")

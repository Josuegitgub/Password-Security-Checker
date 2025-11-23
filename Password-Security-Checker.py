import random
import math
import time
# Definir los conjuntos de caracteres
Letras_Mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
Letras_Minusculas = "abcdefghijklmnñopqrstuvwxyz"
Numeros = "0123456789"
Simbolos = ".,-_!@#$%&*()[]{}<>?/|"
caracteres_posibles = Letras_Mayusculas + Letras_Minusculas + Numeros + Simbolos

# Función para estimar la fuerza de la contraseña
def estimar_fuerza_contrasena(contrasena):
    longitud = len(contrasena)
    
    # Verificar qué tipos de caracteres están presentes
    tiene_mayus = any(c in Letras_Mayusculas for c in contrasena)
    tiene_minus = any(c in Letras_Minusculas for c in contrasena)
    tiene_numeros = any(c in Numeros for c in contrasena)
    tiene_simbolos = any(c in Simbolos for c in contrasena)
    
    # Calcular el tamaño efectivo del conjunto basado en lo usado
    tamano_efectivo = 0
    if tiene_minus:
        tamano_efectivo += len(Letras_Minusculas)
    if tiene_mayus:
        tamano_efectivo += len(Letras_Mayusculas)
    if tiene_numeros:
        tamano_efectivo += len(Numeros)
    if tiene_simbolos:
        tamano_efectivo += len(Simbolos)
    
    # Si no hay variedad, usar al menos minúsculas (asumiendo base)
    if tamano_efectivo == 0:
        tamano_efectivo = len(Letras_Minusculas)
    
    # Número total de combinaciones posibles
    combinaciones = tamano_efectivo ** longitud
    
    # Entropía en bits (fuerza)
    entropia = math.log2(combinaciones) if combinaciones > 0 else 0
    
    # Estimación de tiempo para crackear (asumiendo 1e9 intentos por segundo, típico de hardware moderno)
    intentos_por_segundo = 1e9  # 1 billón de intentos por segundo
    tiempo_segundos = combinaciones / intentos_por_segundo
    tiempo_dias = tiempo_segundos / (60 * 60 * 24)
    tiempo_meses = tiempo_dias / 30 if tiempo_dias > 30 else 0
    tiempo_anos = tiempo_meses // 12 if tiempo_meses > 12 else 0
    
    # Clasificar la fuerza
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

# Pedir la contraseña al usuario
contrasena = input("Ingresa tu contraseña para verificar su seguridad: ")

# Verificar si la contraseña está en el conjunto de caracteres
if not all(c in caracteres_posibles for c in contrasena):
    print("La contraseña contiene caracteres no soportados. Solo se admiten letras mayúsculas, minúsculas, números y símbolos especificados.")
    exit()

# Menú de opciones
print("\nElige una opción para verificar la contraseña:")
print("1. Verificación aleatoria (genera intentos aleatorios hasta coincidir)")
print("2. Verificación inteligente (construye la contraseña carácter por carácter, fijando los correctos)")
opcion = input("Ingresa 1 o 2: ").strip()

if opcion == "1":
    # Opción 1: Verificación aleatoria
    print("\nIniciando verificación aleatoria...")
    print("Nota: Se mostrarán actualizaciones cada 10,000 intentos para evitar saturar la pantalla. Si la contraseña es encontrada, se detendrá.")
    
    contador = 0
    while True:
        attempt = ''.join(random.choice(caracteres_posibles) for _ in range(len(contrasena)))
        contador += 1
        
        if contador % 10000 == 0:
            print(f"Intentos realizados: {contador}, probando actualmente: {attempt}")
        
        if attempt == contrasena:
            print(f"\n¡Contraseña decifrada en {contador} intentos! Es: {attempt}")
            break

elif opcion == "2":
    # Opción 2: Verificación inteligente
    print("\nIniciando verificación inteligente...")
    print("Nota: Se mostrarán los intentos para cada posición hasta encontrar el carácter correcto.")
    
    contador = 0
    contrasena_descifrada = ""
    
    for i in range(len(contrasena)):
        print(f"\nBuscando el carácter en la posición {i+1}...")
        for char in caracteres_posibles:
            attempt = contrasena_descifrada + char + "?" * (len(contrasena) - i - 1)  # Mostrar progreso con ? para posiciones no probadas
            contador += 1
            print(f"Intento {contador}: Probando '{attempt}'")
            time.sleep(0.01)  # Pequeña pausa para mejor visualización
            
            if char == contrasena[i]:
                contrasena_descifrada += char
                print(f"¡Carácter encontrado! Ahora la contraseña parcial es: '{contrasena_descifrada}'")
                break
    
    print(f"\n¡Contraseña completamente decifrada en {contador} intentos! Es: {contrasena_descifrada}")

else:
    print("Opción no válida. Saliendo.")
    exit()

# Mostrar análisis de fuerza de la contraseña
resultado = estimar_fuerza_contrasena(contrasena)
print(f"\nAnálisis de la contraseña '{contrasena}':")
print(f"Longitud: {resultado['longitud']}")
print(f"Tamaño del conjunto de caracteres usado: {resultado['tamano_conjunto']}")
print(f"Número de combinaciones posibles: {resultado['combinaciones']:.2g}")
print(f"Entropía (fuerza en bits): {resultado['entropia_bits']:.2g}")
print(f"Clasificación: {resultado['clasificacion']}")
print(f"Tiempo estimado para crackear (segundos): {resultado['tiempo_estimado_segundos']}")
print(f"Tiempo estimado para crackear (días): {int(resultado['tiempo_estimado_dias'])}")
print(f"Tiempo estimado para crackear (meses): {int(resultado['tiempo_estimado_meses'])}")
print(f"Tiempo estimado para crackear (años): {int(resultado['tiempo_estimado_anos'])}")

print("\nRecuerda: Esta simulación es educativa. En la realidad, las contraseñas se almacenan hasheadas y salteadas, lo que hace el cracking mucho más difícil.")
print("Nota: Esta es una estimación simplificada. La seguridad real depende de muchos factores. Usa contraseñas únicas y considera gestores de contraseñas.")

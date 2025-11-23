# Verificador de Seguridad de Contraseñas

## Descripción
Este proyecto es un script en Python que simula un verificador de seguridad de contraseñas. Permite al usuario ingresar una contraseña y elegir entre dos métodos para "crackearla" de manera simulada: uno aleatorio (brute-force puro) y otro inteligente (construyendo carácter por carácter). Además, proporciona un análisis detallado de la fuerza de la contraseña, incluyendo entropía, combinaciones posibles y tiempos estimados para crackearla.

**Nota importante**: Este es un proyecto educativo para demostrar conceptos de seguridad de contraseñas. No se debe usar para intentar crackear contraseñas reales, ya que viola leyes de privacidad y ética. En la realidad, las contraseñas se almacenan hasheadas, lo que hace el cracking prácticamente imposible.

## Características
- **Validación de caracteres**: Soporta letras mayúsculas/minúsculas (incluyendo "Ñ"), números y símbolos comunes.
- **Dos modos de verificación**:
  - **Aleatoria**: Genera intentos aleatorios hasta coincidir con la contraseña. (Similar a un ataque de fuerza bruta)
  - **Inteligente**: Construye la contraseña fijando caracteres correctos uno por uno.
- **Análisis de fuerza**: Calcula longitud, conjunto de caracteres usado, combinaciones posibles, entropía en bits y clasificación (Muy débil, Débil, Moderada, Fuerte, Muy fuerte).
- **Estimaciones de tiempo**: Proporciona tiempos estimados en segundos, días, meses y años (como enteros), asumiendo 1 billón de intentos por segundo en hardware moderno.
- **Visualización**: Muestra progreso en pantalla, con pausas en el modo inteligente para mejor experiencia.
- **Advertencias educativas**: Recuerda que las contraseñas reales son seguras debido a hashing y salting.

## Requisitos
- Python 3.x (probado en Python 3.8+).
- Módulos estándar: `random`, `math`, `time` (ya incluidos en Python).

## Instalación
1. Clona este repositorio:
2. ```$ Git clone https://github.com/tu-usuario/verificador-contrasenas.git```
3. Navega al directorio del proyecto:
4. ```$CD Verificador-Contrasenas```
5. Ejecuta el script directamente (no requiere instalación adicional):
6. ```Python Password-Security-Checker.py```

## Uso
1. Ejecuta el script con `python Password-Security-Checker.py`.
2. Ingresa tu contraseña cuando se te pida.
3. Elige una opción:
- **1**: Verificación aleatoria (puede tomar mucho tiempo para contraseñas largas).
- **2**: Verificación inteligente (eficiente, encuentra la contraseña en pocos intentos).
4. Observa el proceso en pantalla y el análisis final.

### Ejemplos
- **Contraseña simple** (ej. "abc"):
- Opción 1: Puede encontrar en pocos intentos aleatorios.
- Opción 2: Encuentra rápidamente probando caracteres por posición.
- Análisis: Clasificación "Muy débil", tiempos bajos.

- **Contraseña compleja** (ej. "P@ssw0rd123!"):
- Opción 1: Probablemente no termine en tiempo razonable.
- Opción 2: Encuentra en ~10-20 intentos.
- Análisis: Clasificación "Fuerte", tiempos estimados altos (años).

## Contribuciones
¡Las contribuciones son bienvenidas! Si quieres mejorar el código (ej. agregar más caracteres, optimizar cálculos o traducir a otros idiomas), sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcion`.
3. Haz commit de tus cambios: `git commit -m "Agrega nueva función"`.
4. Push a la rama: `git push origin feature/nueva-funcion`.
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Disclaimer (Liberación de Responsabilidad)
Este proyecto ha sido desarrollado únicamente con fines éticos y educativos, para demostrar conceptos de seguridad informática y criptografía. El autor no se hace responsable de cualquier uso indebido, ilegal o no ético de esta herramienta. No se debe utilizar para intentar crackear, acceder o comprometer contraseñas reales de terceros, ya que esto viola leyes de privacidad, protección de datos y ética digital. El usuario asume toda la responsabilidad por el uso que le dé a este código. Recuerda: en la práctica, las contraseñas se protegen con hashing y salting, haciendo el cracking real inviable.

## Créditos
- Desarrollado por @Josuegitgub como proyecto educativo.
- Inspirado en conceptos de criptografía y seguridad informática.
- Agradecimientos a la comunidad de Python por los módulos estándar.

## Contacto
Si tienes preguntas o sugerencias, abre un issue en GitHub.

¡Gracias por usar este proyecto! Recuerda: 
La mejor seguridad es usar contraseñas únicas y gestores de contraseñas. 🔒

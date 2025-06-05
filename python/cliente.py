import requests
import time

# La URL del servidor dentro de la red Docker Compose
# 'servidor' es el nombre del servicio en docker-compose.yml
URL_SERVIDOR = "http://servidor:8000/"

print("--- Iniciando el programa cliente ---")

try:
    # Intenta conectar con el servidor varias veces.
    # Esto es útil si el servidor tarda un poco en arrancar.
    for i in range(5): # Intentará conectar 5 veces
        print(f"Intento {i+1}: Conectando al servidor en {URL_SERVIDOR}...")
        # Se añade un timeout para que la conexión no se quede colgada indefinidamente.
        response = requests.get(URL_SERVIDOR, timeout=5)

        # Si la respuesta es exitosa (código 200 OK)
        if response.status_code == 200:
            print("¡Conexión exitosa con el servidor!")
            print(f"El servidor respondió con el código de estado: {response.status_code}")
            # Puedes imprimir una parte del contenido de la respuesta (HTML) si quieres,
            # pero el cliente no lo va a "procesar" como una página web.
            # print(f"Contenido recibido del servidor (primeras 100 caracteres):\n{response.text[:100]}...")
            break # Sale del bucle una vez que la conexión es exitosa
        else:
            print(f"Servidor respondió con estado {response.status_code}. Reintentando en 3 segundos...")
            time.sleep(3) # Espera antes de reintentar

    else:
        # Si el bucle termina sin un 'break' (es decir, no se pudo conectar)
        print("No se pudo conectar con el servidor después de varios intentos.")

# Manejo de excepciones para diferentes tipos de errores de conexión
except requests.exceptions.ConnectionError:
    # Error si el servidor no está accesible.
    print(f"ERROR: No se pudo establecer conexión con el servidor en {URL_SERVIDOR}. Asegúrate de que el servidor esté corriendo.")
except requests.exceptions.Timeout:
    # Error si la conexión excede el tiempo de espera.
    print("ERROR: La conexión con el servidor ha excedido el tiempo de espera.")
except Exception as e:
    # Cualquier otro error inesperado.
    print(f"Ocurrió un error inesperado al intentar conectar: {e}")

print("--- Cliente finalizado ---")

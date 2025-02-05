import subprocess

# Función para ejecutar comandos en la terminal
def ejecutar_comando(comando):
    try:
        subprocess.run(comando, check=True, shell=True)
        print(f"Comando '{comando}' ejecutado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando '{comando}': {e}")
        exit(1)

# Ejecutar los comandos en orden
comandos = [
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py runserver 0.0.0.0:8000"
]

for comando in comandos:
    ejecutar_comando(comando)

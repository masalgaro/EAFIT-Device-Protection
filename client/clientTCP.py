## Client program that connects with serverTCP.

import socket

print("[INFO]Este es el programa para los clientes/dispositivos de uso público en la universidad.\n")
host = socket.gethostname()
port = 21115
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))
while True:
    try:
        cliente.sendall(f'{host}') # Send the host name directly.
        data = cliente.recv(1024)
    
    except socket.error:
        print("[ERROR]Error de socket.")
        break
cliente.close()
print("[INFO]Terminando programa del cliente.\nEjecute el script nuevamente para que el servidor pueda rastrear el dispositivo de forma correcta.")


## Client program that connects with serverTCP.

import socket, time

print("[INFO]Este es el programa para los clientes/dispositivos de uso público.\n")

while True:
    host = socket.gethostname()
    hostSend = bytes(host, "utf-8")
    port = 21115
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('0.0.0.0', port))
    try:
        cliente.sendall(hostSend) # Send the host name directly.
        print("[DEBUG]Enviado el nombre del host al servidor.\n")
        data = cliente.recv(1024)
        print("[DEBUG]Recibido ", data, " del servidor.\n")
        time.sleep(10)
    
    except socket.error:
        print("[ERROR]Error de socket.\n")
        break

cliente.close()
print("[ALERTA]Terminando programa del cliente.\nEjecute el script nuevamente para que el servidor pueda rastrear el dispositivo de forma correcta.")

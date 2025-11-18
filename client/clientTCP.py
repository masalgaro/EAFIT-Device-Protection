## Client program that connects with serverTCP.

import socket, time, sys

if len(sys.argv) < 1:
    print("[ERROR]El programa requiere que se agregue una dirección IP para el servidor al ejecutarse.")
    print("[ERROR]El método de ejecución debe ser similar a: python3 clientTCP.py 127.0.0.1")
    sys.exit(1)

print("[INFO]Este es el programa para los clientes/dispositivos de uso público.\n")
serverAddr = ''
serverAddr = sys.argv[1]
print(f"[INFO]El cliente va a conectarse al servidor con la dirección IP {serverAddr}")
while True:
    host = socket.gethostname()
    hostSend = bytes(host, "utf-8")
    port = 21115
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((serverAddr, port))
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

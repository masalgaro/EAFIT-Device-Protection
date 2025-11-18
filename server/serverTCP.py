## Alternative server program that works using sockets and raw TCP messages.
## Instead of IP addresses this works by storing host names from the socket data. This requires the usage of threading to handle multiple clients at once.

import socket
import threading
import concurrent.futures
import sys
from StoreIP import StoreIPAddress as SIP

MAX_THREAD_AMMOUNT = 20 # Establish a maximum number of threads

def updateHostList(HostNameFile: str) -> list[str] or None:
    try:
        with open(HostNameFile, 'r') as HostList:
            hostnames = HostList.read().splitlines()
            # debug stuff
            print(type(hostnames), hostnames)
            HostList.close()
            return hostnames
    except:
        print("Error accediendo a la lista de nombres de host.")
        return


def echoClients(interface: str, port: int) -> None:
    s.listen(5)
    while True:
        conn, address = s.accept()
        print(f"[INFO]Conectado con {address}\n")
        try:
            data = conn.recv(1024) # Receive the host name of the client
            if not data:
                print(f"[ALERTA]Socket {conn} de la dirección {address} NO responde y puede estar en riesgo.\n")
            else:
                print("[DEBUG]Mensaje recibido: ", data, "\n") # Data should be the host name of the client we're connected to
                SIP.writeClientInfo(IPaddress=data, IPstorageFile=archivoHosts) # Add the host to the storage file
                pass # Skip ahead to the next call of this function

        except socket.error:
            print("[ERROR]Error de socket.\n")

        finally:
            conn.close()
    
        print("[DEBUG]Conexión Terminada")
        pass


if __name__ == "__main__":
    print("[INFO]Esta versión del programa funciona con sockets TCP, y requiere que cada host tenga un proceso de cliente activo en todo momento.\n")
    archivoHosts = ''

    if len(sys.argv) < 1: # Specifies a name for the storage file.
        archivoHosts = sys.argv[1]
    else:
        archivoHosts = "Hosts-Conocidos.txt" # Different name from the version of the server that uses IP addresses.
    SIP.defineStorageFile(fileName=archivoHosts)

    host = '0.0.0.0' # We will listen from all interfaces
    port = 21115 # Just a random socket that isn't well-known or widely used.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Can reuse the port
    s.bind((host, port))
    print(f"[INFO]Servidor conectado en la interfaz {host}, y el puerto: {port}")

    for i in range(MAX_THREAD_AMMOUNT):
        i = threading.Thread(target=echoClients, args=(host, port))
        i.start()
        
## Alternative server program that works using sockets and raw TCP messages.
## Instead of IP addresses this works by storing host names from the socket data. This requires the usage of threading to handle multiple clients at once.

import socket
import threading # Added in 3.14
import sys # Para leer los argumentos. 
import StoreIP as SIP

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


def socketPing(interface: str, port: int) -> None:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print(f"{host}, {port}")

    s.listen(2)
    conn, address = s.accept()
    print(f"Conectado con {address}")
    while True:
        try:
            data = conn.recv(1024)
            if not data: break

            print("Mensaje recibido: ", data)
            conn.sendall("Holi")

        except socket.error:
            print("Error de socket.")
            break

    conn.close()


if __name__ == "__main__":
    print("[INFO]Esta versión del programa funciona con sockets TCP, sin embargo requiere que cada host tenga un proceso de cliente activo en todo momento.")
    clientesActivos = []
    archivoHosts = ''

    if len(sys.argv) < 1: # Specifies a name for the storage file.
        archivoHosts = sys.argv[1]
    else:
        archivoHosts = "Hosts-Conocidos.txt"
    SIP.defineStorageFile(archivoHosts)

    host = '' # We will listen from all interfaces
    port = 21115 # Just a random socket that isn't well-known or widely used.
    #socketPing(interface=host, port=port)

import socket
import sys
import threading
import time
from StoreIP import StoreIPAddress as SIP

CHECK_INTERVAL = 10          # Cada cuánto revisar inactividad
CLIENT_TIMEOUT = 30          # Si un cliente no envía datos en este tiempo alertar

# Diccionario en memoria para saber último contacto con cada host
last_seen = {}   # { "hostname": timestamp }

def load_known_hosts(archivoHosts: str) -> set[str]:
    """Carga hosts en memoria para evitar duplicados."""
    try:
        with open(archivoHosts, 'r') as f:
            hosts = set(f.read().splitlines())
        print("[DEBUG] Hosts cargados:", hosts)
        return hosts
    except FileNotFoundError:
        return set()


def monitor_clients(known_hosts: set[str]):
    """Revisa periódicamente que los hosts registrados sigan enviando datos."""
    while True:
        time.sleep(CHECK_INTERVAL)

        now = time.time()

        for host in known_hosts:
            if host not in last_seen:
                # Aún no ha enviado nada desde que se cargó el archivo
                continue

            elapsed = now - last_seen[host]

            if elapsed > CLIENT_TIMEOUT:
                print(f"[ALERTA] El cliente '{host}' no ha enviado información en {elapsed:.1f} segundos.\n")


def echoClients(s: socket.socket, archivoHosts: str, known_hosts: set[str]) -> None:
    s.listen(5)
    print("[INFO]Servidor listo para aceptar conexiones...\n")

    while True:
        conn, address = s.accept()
        print(f"[INFO] Conectado con {address}")

        try:
            data = conn.recv(1024)

            if not data:
                print(f"[ALERTA] El socket {address} no envió datos.")
            else:
                print("[DEBUG] Mensaje recibido")

                hostname = data.decode('utf-8', errors='ignore').strip()
                print(f"[DEBUG] Hostname decodificado: '{hostname}'")

                # Registrar última vez visto
                last_seen[hostname] = time.time()

                # Guardar solo si es nuevo
                if hostname not in known_hosts:
                    print(f"[INFO] Nuevo cliente detectado: '{hostname}', guardando...")
                    SIP.writeClientInfo(IPaddress=hostname, IPstorageFile=archivoHosts)
                    known_hosts.add(hostname)
                else:
                    print(f"[INFO] Cliente '{hostname}' ya registrado. No se añade.")

        except socket.error as e:
            print("[ERROR] Error de socket:", e)

        finally:
            conn.close()
            print("[DEBUG] Conexión terminada\n")


if __name__ == "__main__":
    print("[INFO]Servidor con detección de duplicados e inactividad.\n")

    # Archivo de almacenamiento
    archivoHosts = sys.argv[1] if len(sys.argv) > 1 else "Hosts-Conocidos.txt"
    SIP.defineStorageFile(fileName=archivoHosts)

    # Cargar lista inicial (evitar duplicados)
    known_hosts = load_known_hosts(archivoHosts)

    host = "0.0.0.0"
    port = 21115

    # Configurar socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    print(f"[INFO]Servidor iniciado en {host}:{port}\n")

    # Hilo que monitoriza inactividad
    threading.Thread(target=monitor_clients, args=(known_hosts,), daemon=True).start()

    # Main server loop
    echoClients(s, archivoHosts, known_hosts)

import socket
import time
import sys

def main():

    # 1. Validar argumentos
    if len(sys.argv) < 2:
        print("[ERROR] Uso correcto: python3 clientTCP.py <IP_del_servidor>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = 21115

    print("[INFO] Cliente TCP iniciado.")
    print(f"[INFO] Conectándose al servidor en {server_ip}:{server_port}")

    # Obtener nombre del host
    hostname = socket.gethostname()
    hostname = "PC_33-202"
    hostname_bytes = hostname.encode("utf-8")


    while True:
        cliente = None
        try:
            # 2. Crear socket
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(10)  # evita bloqueos eternos

            # 3. Intentar conexión
            cliente.connect((server_ip, server_port))
            print("[DEBUG] Conectado con éxito al servidor.")

            # 4. Enviar nombre del host
            cliente.sendall(hostname_bytes)
            print(f"[DEBUG] Enviado nombre del host: {hostname}")

            # 5. Esperar 10 segundos antes del siguiente ciclo
            time.sleep(10)

        except (socket.timeout, ConnectionRefusedError) as e:
            print(f"[ERROR] No se pudo conectar: {e}")
            print("[INFO] Reintentando conexión en 5 segundos...")
            time.sleep(5)

        except Exception as e:
            print(f"[ERROR] Excepción inesperada: {e}")
            print("[INFO] Abortando cliente.")
            break

        finally:
            if cliente:
                cliente.close()

if __name__ == "__main__":
    main()

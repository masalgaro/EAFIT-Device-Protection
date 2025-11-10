## Main server program: it will send pings to all stored IPs

from icmplib import ping, multiping
from StoreIP import StoreIPAddress as SIP 

def updateIPList(IPAddressFile: str) -> list[str] or None:
    try:
        with open(IPAddressFile, 'r') as addressList:
            IPs = addressList.read().splitlines()
            # debug stuff
            print(type(IPs), IPs)
            addressList.close()
            return IPs
    except:
        print("Error accediendo a la lista de direcciones IP")
        return

def pingKnownIPs(IPList: list[str]) -> int:
    deadHosts = 0
    if (len(IPList) > 1):
        print("Haciendo ping a las IPs guardadas...")
        hosts = multiping(IPList, count=5, interval=0.6, timeout=3, privileged=False)
        for host in hosts:
            if not host.is_alive:
                print("================ALERTA================")
                print(f"{host.address} no responde")
                print("================ALERTA================")
                deadHosts += 1
        print("Pings y checkeos finalizados.")
        if deadHosts != 0:
            print(f"Hay {deadHosts} clientes que no responden y pueden estar en riesgo.")
        return deadHosts
    elif (len(IPList) == 0):
        print("No hay ninguna IP guardada en la lista.")
        return deadHosts
    print("Haciendo ping a la IP guardada.")
    cliente = ping(IPList, count=5, interval=0.6, timeout=3, privileged=False)
    if not cliente.is_alive:
        print("================ALERTA================")
        print(f"{cliente.address} no responde")
        print("================ALERTA================")
        deadHosts += 1
    return deadHosts

            

# The actual listening to IPs thing should happen always so idk if a separate function would really be needed.
if __name__ == "__main__":
    arcihvoPrueba = "Direcciones.txt"
    SIP.defineStorageFile(arcihvoPrueba)
    SIP.writeIPAddress(IPaddress="127.0.0.1", IPstorageFile=arcihvoPrueba)
    SIP.writeIPAddress(IPaddress="1.1.1.1", IPstorageFile=arcihvoPrueba)
    listaIP = updateIPList(arcihvoPrueba)
    pingKnownIPs(listaIP)


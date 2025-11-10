## Main server program: it will send pings to all stored IPs

import icmplib as icmp
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
    print("Haciendo ping a las IPs guardadas...")
    hosts = icmp.multiping(IPList, count=1, interval=0.5, timeout=3)
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
            

# The actual listening to IPs thing should happen always so idk if a separate function would really be needed.
if __name__ == "__main__":
    SIP.defineStorageFile("Direcciones.txt")
    if (SIP.writeIPAddress("127.0.0.1", "Direcciones.txt") == 1):
        print("Funciona correctamente")
    else:
        print("Vida hp")

## Main server program: it will send pings to all stored IPs

import icmplib as icmp
from StoreIP import StoreIPAddress as SIP 

def updateIPList(IPAddressFile: str) -> None:
    try:
        with open(IPAddressFile, 'r') as addressList:
            IPs = addressList.read().splitlines()
            # debug stuff
            print(type(IPs), IPs)
    except:
        print("Error accediendo a la lista de direcciones IP")
        
    pass

def pingKnownIPs(IPAddressFile: str) -> None:
    pass

# the actual listening to IPs thing should happen always so idk if a separate function would really be needed.


if __name__ == "__main__":
    SIP.defineStorageFile("Direcciones.txt")
    if (SIP.writeIPAddress("127.0.0.1", "Direcciones.txt") == 1):
        print("Funciona correctamente")
    else:
        print("Vida hp")

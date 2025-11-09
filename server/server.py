# Main server program: it will send pings to all stored IPs
# Needs a way to store IPs in a file it can read over and over

import icmplib as icmp
from StoreIP import StoreIPAddress as SIP 

SIP.defineStorageFile("Direcciones.txt")
if (SIP.writeIPAddress("127.0.0.1", "Direcciones.txt") == 1):
    print("Funciona correctamente")
else:
    print("Vida hp")

# let's do the code for reals lmao

def updateIPList(IPAddressFile: str) -> list:
    with open(IPAddressFile, 'r') as addressList:
        IPs = file.read().splitlines()
    pass

def pingKnownIPs(IPlist: str) -> None:
    pass

# the actual listening to IPs thing should happen always so idk if a separate function would really be needed.


# Main server program: it will send pings to all stored IPs
# Needs a way to store IPs in a file it can read over and over

from StoreIP import StoreIPAddress as SIP 

SIP.defineStorageFile("Direcciones.txt")
if (SIP.writeIPAddress("127.0.0.1", "Direcciones.txt") == 1):
    print("Funciona correctamente")
else:
    print("Vida hp")

# lets do the code for reals lmao

def pingKnownIPs():
    pass

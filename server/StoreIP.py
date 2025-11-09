import os
import re

## Handles storage of addresses into a local file, the server will use this file to make a list of all addresses it needs to ping.
class StoreIPAddress:

    def defineStorageFile(fileName: str) -> None:
        if (os.path.isfile(fileName) is False):
            storageFile = open(fileName, 'x')
            print("Archivo de almacenamiento creado correctamente.")
            storageFile.close()
        else:
            print("Archivo de almacenamiento ya existe con este nombre.")
        return

    def writeIPAddress(IPaddress: str, IPstorageFile: str) -> int: # Receives the IP address and returns an int to indicate if it was added succesfully or not
        try:
            with open(IPstorageFile, 'a') as storageFile:
                storageFile.write(IPaddress + "\n")
                storageFile.close()
                return 1 # Returns 1 if everything worked correctly
        except:
            print("Error accediendo al archivo. Error 0")
            return 0 # Returns 0 if it couldn't write the IP address.
    
    def deleteIPAddress(IPaddress: str, IPstorageFile: str) -> int: # Receives the IP address that needs to be deleted from the file
        # first it checks if the IP is in the list
        storageFile = open(IPstorageFile, 'r')
        lines = storageFile.readlines() # Stores all the addresses in a list
        storageFile.close()
        try:
            storageFile = open(IPstorageFile, 'w')
            for line in lines:
                if line.strip("\n") != IPaddress:
                    storageFile.write(line)
            print("IP eliminada de manera correcta.")
            return 0
        except:
            print("Hubo un error al eliminar la IP. Error -1")
            return -1
    
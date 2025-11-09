import os

class StoreIPAddress:

    def defineStorageFile(fileName: str) -> None:
        if (os.path.isfile(fileName) is False):
            storageFile = open(fileName, 'x')
            print("Archivo de almacenamiento creado correctamente.")
            storageFile.close()
        else:
            print("Archivo de almacenamiento ya existe con este nombre.")
        return

    def writeIPAddress(IPaddress: str, IPstorageFile: str) -> int: # it receives the IP address and returns an int to indicate if it was added succesfully or not
        try:
            with open(IPstorageFile, 'a') as storageFile:
                storageFile.write(IPaddress + "\n")
                storageFile.close()
                return 1 # Returns 1 if everything worked correctly
        except:
            print("Error accediendo al archivo. Error 0")
            return 0 # Returns 0 if it couldn't write the IP address.
    
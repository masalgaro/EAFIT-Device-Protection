# EAFIT Device Protection
Una forma de realizar alertas de posibles robos de equipos de la universidad con el suficiente tiempo para tomar acciones preventivas.  
Esta implementación se enfoca en ser ligera y rápida, con el fin de no usar mucho espacio de almacenamiento y reducir el impacto en la banda ancha de la universidad; por esto nuestra implementación no requiere de librerias externas más allá de icmplib.  

## Funcionamiento

Existen dos versiones del programa: una es una edición básica que solo requiere al servidor que funciona comprobando conectividad con direcciones IP conocidas, la otra es una aplicación cliente-servidor que funciona utilizando sockets.  

Al momento de ejecutar cualquiera de las dos versiones, se puede pasar un argumento que índica el nombre del archivo de almacenamiento de la forma:  

```bash
python3 server.py Direcciones.txt # Usando la versión con direcciones IP conocidas
python3 serverTCP.py Host-Conocidos.txt # Usando la versión con sockets
```

### Edición de direcciones IP conocidas

Se encuentra dentro de la carpeta "server" como el archivo `server.py`. Consiste en una aplicación simple que utiliza el protocolo *ICMP* para comprobar la conectividad con direcciones IP que conozca. Para que este programa funcione se deben agregar direcciones IP a una lista, por lo que presenta limitaciones en redes más complejas donde las direcciones IP puedan cambiar. Puede ser una implementación útil en redes locales donde el administrador de la red conoce las direcciones IP de los dispositivos en su interior.  
La ventaja de esta implementación es la facilidad de uso y la eficiencia, ya que la única libreria externa que requiere es **[icmplib](https://pypi.org/project/icmplib/)** para realizar ping, y no se requiere un programa para los clientes, minimizando el consumo de recursos.  

### Edición de cliente-servidor con sockets

El archivo del servidor se encuentra dentro de la carpeta "server" bajo el nombre de `serverTCP.py`, el archivo del cliente se encuentra dentro de "client" como `clientTCP.py`.  
Esta implementación **no usa librerias externas** a las que Python ofrece por defecto, pero sí requiere que todos los dispositivos que se desean monitorear ejecuten y mantengan abierto el programa para el cliente, lo que podría tener impactos menores en el rendimiento.  
La ventaja de esta implementación es que es escalable y versátil en espacios donde las direcciones IP pueden cambiar con el tiempo, ya que en vez de fijarse en una dirección específica se fija en el nombre del host del cliente.  

Para el cliente es necesario pasar como argumento la dirección IP del servidor, de la forma `python3 clientTCP.py [IP_ADDR]` como por ejemplo: `python3 clientTCP.py 127.0.0.1`, esto se hace con el objetivo de tener seguridad de que los dispositivos si envíen la información al servidor de forma correcta y no se crucen los datos con otros clientes.

## Dependencias

El programa usa librerias propias de Python, **con la excepción de [icmplib](https://pypi.org/project/icmplib/)**, que se usa en la versión del server que trabaja con direcciones IP conocidas para realizar pings a los dispositivos que se desean monitorear.  

## Créditos

Este proyecto fue realizado para la clase de **Sistemas de Información** en la Universidad EAFIT por *Miguel Angel Gomez Olarte, Mateo Pineda Alvarez, David Alejandro Ballesteros, y Esteban Alvarez Zuluaga*

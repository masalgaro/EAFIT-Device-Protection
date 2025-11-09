# EAFIT-Device-Protection
Una forma de realizar alertas de posibles robos de equipos de la universidad con el suficiente tiempo para tomar acciones preventivas.  
Esta implementación se enfoca en ser ligera y rápida, con el fin de no usar mucho espacio de almacenamiento y reducir el impacto en la banda ancha de la universidad; por esto nuestra implementación no requiere de librerias externas más allá de icmplib.  

## Funcionamiento

Se presenta un programa para el servidor central (dentro de la carpeta "server"), y un programa para los clientes o computadoras de la universidad (dentro de la carpeta "client").  
**El servidor** se dedica a realizar pings de forma periódica a las direcciones IP que conoce, y escuchar mensajes de los clientes que le índican si debe incluir o excluir su IP de este procedimiento. Si una de las direcciones IP guardadas no responde al ping, el servidor realizará una alerta de un posible robo o daño al equipo.  
**El cliente** envía su dirección IP al servidor para que pueda detectar si sigue prendido o conectado a la red, o bien para decirle al servidor que deje de monitorear el dispositivo, que se debe ejecutar cuándo el equipo se va a apagar de manera órganica o trasladar por personal autorizado. No necesita ejecutarse el programa el resto del tiempo para poder recibir pings del servidor.  

## Dependencias

El programa usa librerias propias de Python, **con la excepción de [icmplib](https://pypi.org/project/icmplib/)** que se utilizó para realizar los pings.  
Se usó ICMP como protocolo débido a lo rápido y liviano que es (como contexto, el comando `ping` en la terminal usa este protocolo).  

## Créditos

Este proyecto fue realizado para la clase de **Sistemas de Información** en la Universidad EAFIT por *Miguel Angel Gomez Olarte, Mateo Pineda Alvarez, David Alejandro Ballesteros, y Esteban Alvarez Zuluaga*

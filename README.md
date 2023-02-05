# 2048
Este reto es una copia del juego “2048” desarrollado en Python. Este juego consiste 
en un tablero de 4x4 donde aleatoriamente aparecerán casillas con números 2 y 4,
estas deben combinarse para sumarse hasta llegar a 2048, solo pueden sumarse 
casillas con el mismo valor, que estén ubicadas sobre el mismo eje siempre, que no 
tengan otro valor entre ellas y que no hayan sido ya sumadas en ese mismo 
movimiento.
Cada que se realiza un movimiento un numero nuevo aparece en algún lugar del 
tablero.
El juego termina cuando el usuario une dos casillas que sumen 2048 o si el tablero 
se queda sin espacios en blanco ni movimientos posibles.
Con este juego las habilidades mentales de ubicación espacial y lógica matemática 
se ven activadas justo lo que se espera de este reto.
Para ver que realmente funcione se hicieron varios casos de prueba

1. Ganar. El programa debe ser capaz de detener el juego y avisarle al 
usuario que ah ganado cuando un movimiento da como resultado la suma 
de dos casillas con valor de 1024 se convierta en una casilla con el numero 
2048 además de guardar el valor 2048 como top score en el archivo 
score.csv

2. Perder. El programa debe ser capaz de detectar cuando los espacios y 
movimientos en el tablero se han agotado, es decir cuando no hay más
ceros en el tablero ni números iguales colindando y reportárselo al usuario. 
Además, debe guardar la casilla con el valor más alto como “tu score” y 
desplegarlo junto con el “Top score”; en caso de ser este el nuevo top 
score, guárdalo en el archivo score.csv

3. Movimientos. cada que se realiza un movimiento todos los numero se 
deben desplazar en la dirección elegida por el usuario. Los números deben 
desplazarse tantas casillas como sea posible y solo se detendrán si las 
casillas continuas están ocupadas por un numero diferente, en caso de ser 
un numero igual estos deben sumarse y seguir desplazándose hasta donde 
el tablero les permita, esta nueva casilla (que es resultado de una suma) no 
puede volver a sumarse en un mismo movimiento

# El código
El programa esta divido como se nos enseño en clase; la primera parte contiene 
las funciones y la segunda el programa principal que llama a esas funciones, es 
una manera cómoda de trabajar.
Las funciones son la parte mas amplia y tardada de realizar en este programa, 
estas incluyen cada uno de los movimientos, la generación del tablero, las 
herramientas necesarias para evaluar los movimientos y el manejo de archivos

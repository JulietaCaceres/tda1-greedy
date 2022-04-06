# Trabajo práctico 1. Greedy

El código correspondiente a este trabajo práctico tiene como objetivo resolver, mediante la estrategia Greedy, el siguiente problema:

>Para una ruta recién inaugurada de “k” kilómetros de longitud se debe construir un conjunto de antenas celulares para cubrir su recorrido. Se recibieron un conjunto de “n” propuestas. Cada propuesta corresponde a la instalación de una antena en una ubicación determinada. Las características de las antenas pueden variar. Sabemos por la información de cada contrato dónde se ubicará la antena y la cantidad de kilómetros que cubrirá de la ruta expresado en un radio de una cantidad de kilómetros desde donde está ubicada.
Nos solicitan seleccionar el menor subconjunto de contratos de forma que toda la ruta quede totalmente cubierta o que informe que esto no es posible.

# Ejecución

Dentro del directorio de la carpeta se debe ejecutar:

<pre><code>xxx@xxx python k ruta_del_archivo</code></pre>

Donde k es el largo de la ruta y ruta_del_archivo es la ruta al archivo de pueba.

Ejemplo:

<pre><code>xxx@xxx python 500 ./contratos.txt </code></pre>

Se obtendrá como resultado una lista óptima con los id de los contratos a contratar.

Ejemplo:

<pre><code>[5, 2, 6]</code></pre>


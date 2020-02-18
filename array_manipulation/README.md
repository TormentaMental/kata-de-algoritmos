## Consigna

https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Nos dan una matriz de 2 dimensiones. 
Básicamente, es un listado de "operaciones" (aka "queries").
Cada query tiene tres valores. Los dos primeros son la posición del principio y del final en donde vamos a operar.
El tercer valor es un número que vamos a sumar a cada elemento dentro del rango dado.

Además del array de queries, nos dan un número que será la longitud del array que tendremos que construir, que debería ser inicializado con ceros.

Una vez obtenido el array, hay que devolver el valor máximo del array.

(es mejor leer la consigna original para entender el planteo)

### Tip

Una vez finalizado el ejercicio vemos que los tests basados en el reloj no pasan. La resolución "es legal" pero algunos tests terminan en timeout. Por lo cual buscamos en la comunidad de qué manera de puede mejorar la performance.

El resultado nos saca de una solución `O(nxm)` y logra una performance de `O(n+m)`. 
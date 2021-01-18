# Clustering

### ¿Qué es el clustering? 

Es la tarea de agrupar objetos por similitud, en grupos o conjuntos de manera que los miembros del mismo grupo tengan características similares. 

![clustering_and_k_means_machine_learning](https://user-images.githubusercontent.com/63415652/104877374-4ddb2d80-591f-11eb-9bc7-c35b1cdd9467.png)

### ¿En que consiste nuestro dataset? 

El dataset consiste en una comparación de varios caramelos según varias de sus propiedades. 

>**_Nota:_** En este readme sólo se mostrarán los resultados, para más detalles ver el código el la carpeta code de este repo.

--- 
 
Para el primer caso se asumió que si sabemos cuántos grupos queremos crear para nuestro resultado final. Vamos a implementar clustering, utilizando 2 algoritmos, Batch K-Means y Mean-Shift. 
 
 
### Batch K-Means 
 
 Veremos la implementación en código, asignando cuantas categorías serán:
 
 ![20](https://user-images.githubusercontent.com/63415652/103444382-72e85480-4c2d-11eb-8e7f-adb190e8ac4a.PNG)
 
 Podemos ver en los resultados, que de la misma tabla del dataset, ahora tenemos una nueva columna que nos dice en cuál de los clusters o grupos quedó finalmente clasificados. 
 
 >**_Conclusión:_** ¿Qué significa eso? Significa que por ejemplo el caramelo 100 Grand que está en el grupo 1 y el caramelo 3 Musketeers que igual está en el grupo 1, se parecen más entre sí, por ejemplo estos 2 que están en el grupo 1, a otro que está en el grupo 3. 
 
### Mean-Shift
 
Ahora el contrario, ya que el anterior asignamos nosotros las categorías, y ahora dejaremos que el algoritmo decida cuántas categorías serán, con la restricción de que deben de ser una cantidad moderada de datos: 
 
![21](https://user-images.githubusercontent.com/63415652/103444599-4df4e100-4c2f-11eb-9d02-7b5e3daae2b9.PNG)
 
Los resultados no deben de ser 100% equivalentes, tendrán diferencias y serán notables. 
 
 >**_Conclusión:_** Utilizando Mean-Shift como algoritmo y sin establecer la cantidad de clústeres o grupos, el algoritmo decidió que lo correcto sería solo crear 3 en vez de 4 como paso con Batch K-Means. Esta cuestión es bastante cuestionable, todo depende en el contexto para que sea verdaderamente útil nuestros análisis.





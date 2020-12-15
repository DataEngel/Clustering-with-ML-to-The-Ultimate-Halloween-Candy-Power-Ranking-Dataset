import pandas as pd

# Importamos el algoritmo 
from sklearn.cluster import MiniBatchKMeans

if __name__ == "__main__":

    # Cargamos el dataset 
    dataset = pd.read_csv('./data/candy.csv') 
    #print(dataset.head(10))  

    # Guardamos todas las columnas excepto el nombre del caramelo que esta guardado en competitorname
    X = dataset.drop('competitorname', axis=1)

    # Agrupamos en 4, pasamos por grupos de 8 
    kmeans = MiniBatchKMeans(n_clusters=4, batch_size=8).fit(X)
    #print("Total de centros: " , len(kmeans.cluster_centers_)) 
    print("="*64)
  
    # Para cada uno de los 85 caramelos que están en este conjunto me va devolver un arreglo con 
    # cada una de las categorias. Esto significa que para el primer caramelo el decidio que pertenecia
    # a la categoría numero 2
    print(kmeans.predict(X))
    # Tomamos este arreglo y lo agregamos al datset original. Solo hay que considerar que la nueva columna 
    # tiene que tener el mismo tamaño del dataframe utlizado anteriormente
    dataset['group'] = kmeans.predict(X) 

    print(dataset) 


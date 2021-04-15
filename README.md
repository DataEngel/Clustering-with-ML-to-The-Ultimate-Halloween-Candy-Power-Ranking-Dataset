# Clustering

### What does our dataset consist of?

The dataset consists of a comparison of various candies based on various of their properties.

>**_Note:_** In this readme only the results will be shown, for more details see the code in the code folder of this repo.

### What is clustering?

It is the task of grouping objects by similarity, into groups or sets so that members of the same group have similar characteristics.

![clustering_and_k_means_machine_learning](https://user-images.githubusercontent.com/63415652/104877374-4ddb2d80-591f-11eb-9bc7-c35b1cdd9467.png)

--- 
 
For the first case it was assumed that if we know how many groups we want to create for our final result. We are going to implement clustering, using 2 algorithms, Batch K-Means and Mean-Shift.
 
 
### Batch K-Means 

We will see the implementation in code, assigning how many categories will be:
 
 ![20](https://user-images.githubusercontent.com/63415652/103444382-72e85480-4c2d-11eb-8e7f-adb190e8ac4a.PNG)
 
We can see in the results that from the same table of the dataset, we now have a new column that tells us in which of the clusters or groups it was finally classified.
 
 >**_Conclusion:_** What does that mean? It means that for example the 100 Grand candy that is in group 1 and the 3 Musketeers candy that is still in group 1, are more similar to each other, for example these 2 that are in group 1, to another that is in the Group 3.
 
### Mean-Shift
 
Now the opposite, since the previous one we assigned the categories, and now we will let the algorithm decide how many categories there will be, with the restriction that they must be a moderate amount of data:
 
![21](https://user-images.githubusercontent.com/63415652/103444599-4df4e100-4c2f-11eb-9d02-7b5e3daae2b9.PNG)
 
The results should not be 100% equivalent, they will have differences and will be notable.
 
 >**_Conclusion:_** Using Mean-Shift as algorithm and without establishing the number of clusters or groups, the algorithm decided that the correct thing would be to only create 3 instead of 4 as a step with Batch K-Means. This question is quite questionable, it all depends on the context for our analysis to be truly useful.
 
 ## Data source: [The Ultimate Halloween Candy Power Ranking](https://www.kaggle.com/fivethirtyeight/the-ultimate-halloween-candy-power-ranking) 

Although the code is not proprietary and is free to use, the data is licensed, please read it before using this data.
This project is not for commercial purposes, it is for academic purposes only.

## You can check the main notebook in my kaggle profile and if you like, my other contributions too: 

* [The Ultimate Halloween Candy Power Ranking Notebook](https://www.kaggle.com/dataengel/the-ultimate-halloween-candy-power-ranking) 


#https://leetcode.com/problems/recyclable-and-low-fat-products/
# 1757. Recyclable and Low Fat Products

""" Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable. """

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtro = (products["low_fat"] == "Y") & (products["recyclable"] == "Y")

    return products[filtro][["product_id"]]
#----------------------------------------------------------------

#https://leetcode.com/problems/invalid-tweets/description/
# 1683. Invalid Tweets

""" Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.
 

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.
 """
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame)-> pd.DataFrame:
    #aplicar un metodo a una columna. A una serie se le pueden aplicar operaciones
    filtro = tweets["content"].apply(len) > 15
    #print(tweets[filtro]["tweet_id"])
    return tweets[filtro][["tweet_id"]]
     
    

""" 
def longitud(x):
    return len(x)
#para convertirlo en una funcion lamda
lambda x: len(x) 
"""
#map(int, input().split()) #convertir los elementos a un entero
#map(len, input().split())
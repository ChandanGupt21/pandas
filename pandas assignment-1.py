#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# Q1

# In[15]:


data =[4, 8, 15, 16, 23, 42]
df = pd.Series(data)
print(df)


# Q2

# In[16]:


data =  ["sarfraj" , "abshar" , "abhishek" , "faizan" , "hammad" , "asif" , "arsalan" , "faiz" , "nesat" ,"nemat"]
df2=pd.Series(data)
print(df2)


# Q3

# In[17]:


df3  =pd.DataFrame({'Name': ['Alice' ,  'Bob' ,  'Claire'],

        'Age': [25, 30, 27],

        'Gender': ['Female', 'Male', 'Female']})
print(df3)


# Q4

# In[18]:


In Pandas, a DataFrame is a two-dimensional labeled data structure with columns of potentially 
        different data types. It is similar to a spreadsheet  or a  SQL table. In a DataFrame , data is 
        organized in rows and columns, where each column can be considered as a Pandas Series.

        On the other hand, a Series in Pandas is a one-dimensional labeled array that can contain data of any 
        data type, including integers, strings, and floating-point numbers. It is similar to a column in a 
        spreadsheet or a SQL table.

        The main difference between a DataFrame and a Series is that a DataFrame is a two-dimensional data 
        structure with rows and columns, while a Series is a one-dimensional data structure with only one column.
        Here's an example to illustrate the difference between a DataFrame and a Series:

        Suppose we have the following data:
        Name(Alice , Bob, Charlie) , Age(25, 3, 35) , Gender (Female,Male ,Male)
        We can represent this data using a DataFrame in Pandas as follows:'''
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
       'Age': [25, 30, 35],
       'Gender': ['Female', 'Male', 'Male']}

df = pd.DataFrame(data)

print(df)
     Name  Age  Gender


# In[ ]:


#Q.5> What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
     #you give an example of when you might use one of these functions?

    # 1. head() and tail(): These functions are used to view the first and last n rows of a DataFrame, 
    #    respectively. They can be useful for quickly getting a sense of what the data looks like.
     #   Example:
import pandas as pd

df = pd.read_csv('data.csv')

# View the first 5 rows
print(df.head())

# View the last 5 rows
print(df.tail())
    
   # 2. describe(): This function provides a statistical summary of the DataFrame, including the count, 
    #    mean, standard deviation, minimum, and maximum values, among others.
     #   Example:
import pandas as pd

df = pd.read_csv('data.csv')

# Get a statistical summary of the DataFrame
print(df.describe())

    # 3. groupby(): This function is used to group data in a DataFrame based on one or more columns. 
     #   It can be useful for calculating aggregate statistics for different groups.
      #  Example:
import pandas as pd

df = pd.read_csv('data.csv')

# Group the data by the 'category' column and calculate the mean of the 'value' column
grouped = df.groupby('category').mean()

print(grouped)

   #  4. sort_values(): This function is used to sort the rows of a DataFrame based on one or more columns.
    # Example:
import pandas as pd

df = pd.read_csv('data.csv')

# Sort the DataFrame by the 'value' column in descending order
sorted_df = df.sort_values('value', ascending=False)

print(sorted_df)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'Panel')
Ans> In Pandas, both Series and DataFrame are mutable in nature, while Panel is considered deprecated 
     and has been replaced by multi-dimensional arrays, such as numpy.ndarray or xarray.DataArray, 
     which are also mutable.

     In a mutable object, the contents of the object can be modified after it is created. This means 
     that you can add, remove, or update elements in a Series or DataFrame after they are created.


# In[ ]:


#Q.7> Create a DataFrame using multiple Series. Explain with an example.
import pandas as pd

# Create a Series for each column of data
names = pd.Series(['Alice', 'Bob', 'Charlie', 'David', 'Emily'])
ages = pd.Series([25, 30, 35, 40, 45])
genders = pd.Series(['Female', 'Male', 'Male', 'Male', 'Female'])

# Combine the Series into a DataFrame
df = pd.DataFrame({'Name': names, 'Age': ages, 'Gender': genders})

# Print the resulting DataFrame
print(df)


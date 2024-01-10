#!/usr/bin/env python
# coding: utf-8

# # Project :- Diwali Sales Analysis

# - import python libraries

# ### Pandas

# - Pandas:- Pandas is a library used to work with Data-Set.
# - Pandas has Functions for Analyzing,Cleaning,Exploring & Manipulating data.

# In[34]:


import pandas as pd # used for dataSet/data frame


# ### NumPy

# - NumPy:- NumPy library is used to perform Mathematical Operation on Arrays.

# In[35]:


import numpy as np # used for array , numeric calulation.


# ### Matplotlib

# - Matplotlib :- Matplotlib library is used to create Graphs & Plots.
# - Matplotlib library is help to visualize with data   

# In[36]:


import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Seaborn

# - Seaborn :- Seaborn library is used in visualizing data. 

# In[37]:


import seaborn as sns


# ### Importing the csv file

# In[38]:


# df is a variable where we have stored Whole loaded Data-Set

df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')


# ### df.shape

# - It Shows No. of Row-Coloumn

# In[39]:


df.shape


# ### df.head()

# - This command will show the by default first 5 rows of the loaded DataSet.

# In[40]:


df.head()


# ### df.head(10)

# - This command will show the first 10 rows from the loaded DataSet.

# In[41]:


df.head(10)


# ### df.info()

# - This command will provide us basic information about the DataFrame.

# In[42]:


df.info()


# ### df.drop()

# - Drop command is used to remove unrelated/blank/null columns.
 In above cell we have got two null Column.
  13  Status            0 non-null      float64
  14  unnamed1          0 non-null      float64
  So, We have to remove null values.
# In[43]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# ### After removing these two(['Status', 'unnamed1']) columns.
 13  Status            0 non-null      float64
 14  unnamed1          0 non-null      float64
# In[44]:


df.info()


# ### pd.isnull(df).sum()

# - isnull command is used to check for null values.

# In[45]:


pd.isnull(df).sum()


# ### In above cell there are 12 null values in Amount column so we have to remove it.

# ### df.dropna(inplace=True)

# - dropna command is used to remove null values

# In[46]:


df.dropna(inplace=True)


# ### After removing Amount_Column's null value.

# In[47]:


pd.isnull(df).sum()


# ### astype('Data_Type_Name')

# - Used to Change one data type to another

# In[48]:


df['Amount'] = df['Amount'].astype('int')


# In[49]:


df['Amount'].dtypes


# ### df.columns

# - Show all coloumn

# In[50]:


df.columns


# ### df.rename(columns={column_name})

# - This command is used to Rename the column

# In[51]:


df.rename(columns={'Marital_Status':'Shaadi'})


# ### df.describe()

# - describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)

# In[52]:


df.describe()


# ### use describe() for specific columns

# In[53]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# ### 1. Gender

# In[54]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# - Above chart is showing how many Male and Female in our loaded dataset.

# ### 2. Plotting a bar chart for gender vs total amount

# In[55]:


# In Tabular form
df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[56]:


# In Chart form
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# *From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men*

# ### 3. Age

# In[57]:


sns.countplot(data = df, x = 'Age Group')


# - From above graphs we can see that most of the buyer's age group are 26 - 35

# In[58]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# ### 4. Total Amount vs Age Group

# In[59]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*

# ### 5. State vs Orders

# In[60]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# - From above graphs we can see that what are the total number of orders from top 10 states

# ### 6. State Vs Amount

# In[61]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# *From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*
# 

# ### 7. Marital Status

# In[62]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# - From above graphs we can see that most of the buyers are of Married person.

# ### 8. Marital_Status vs Amount

# In[63]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# ### 9. Occupation vs Count

# In[64]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# - From above graphs we can see that Occupation of IT Sector is highest.

# ### 10. Occupation vs Amount

# In[65]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# ### 11. Product Category vs count

# In[66]:


sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# - From above graphs we can see that the highest purchasing is Clothing Items.

# ### 12. Product_Category vs Amount

# In[67]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# ### 13. Product_ID vs Orders

# In[68]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# - From above graphs we can see that in which Product_ID has highest Orders.

# In[69]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## Conclusion:
# 
# ### 

# *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# I have completed this projet with the help of online resourses and plateform.

# Name - Aatish Kumar Baitha

# M.Tech(Data Science 2nd Year Student)

# #### My Linkedin Profile - 
# www.linkedin.com/in/aatish-kumar-baitha-ba9523191

# #### My Blog -
# https://computersciencedatascience.blogspot.com/

# ### Thank you!

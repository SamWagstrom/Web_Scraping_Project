#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page= requests.get(url)

soup= BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find('table')


# In[10]:


soup.find_all('table')[1]


# In[12]:


soup.find('table', class_='wikitable sortable')


# In[28]:


World_Titles=table.find_all('th')


# In[29]:


world_table_titles = [title.text.strip() for title in World_Titles]


# In[30]:


print(world_table_titles)


# In[31]:


import pandas as pd


# In[33]:


df = pd.DataFrame(columns=world_table_titles)

df


# In[ ]:





# In[34]:


column_data = table.find_all('tr')


# In[37]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[38]:


df


# In[40]:


df.to_csv(r'C:\Users\Sam\Documents\Data Scraping tutorial\web_scraping_tutorial.csv', index= False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





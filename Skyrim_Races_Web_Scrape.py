#!/usr/bin/env python
# coding: utf-8

# # Importing my Libraries

# In[33]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Web Scrape Time

# The table of interest comes from the comparison of races and their skills in one of my favorite games, The Elder Scrolls V: Skyrim.

# In[2]:


url = 'https://elderscrolls.fandom.com/wiki/Races_(Skyrim)'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


print(soup.prettify())


# Make sure to add the style part because without it, the table retrieved will be the one that talks about the different races and their unique powers/effects

# In[9]:


soup.find('table', class_ = 'wikitable', style = "text-align:center; width:100%;")


# In[11]:


table = soup.find_all('table')[1]


# Here I want to get the column headers (or their titles)

# In[14]:


race_titles = table.find_all('th')


# In[15]:


race_titles


# In[17]:


race_table_titles = [title.text.strip() for title in race_titles]

print(race_table_titles)


# # Working with a Dataframe

# I successfully retrieved the titles but I still need to make some minor tweaks because all the titles were thrown into one long horizontal header. What I want is the races to go across and the skills to down the table.

# In[19]:


df = pd.DataFrame(columns = race_table_titles)

df


# With this code, I am specifying where to start my headers so I can keep the layout and data intact.

# In[29]:


df = pd.read_html(str(table), header=[0])[0]
df


# I wanted to get rid of my index numbers but as you can see, without the indices, the table gets all wonky and loses its integrity.

# In[25]:


print(df.to_string(index=False))


# I am renaming my column because the arrows, while helpful, just seem a little wonky.

# In[54]:


df = df.rename(columns={'Races → Skills ↓': 'Skills'})
df


# # Visualization Time

# I felt that a bar plot would work well for this type of data.

# In[55]:


plt.figure(figsize=(15, 8))
sns.barplot(data=df,
            x="Skills",
            y="Altmer")
plt.title('Altmer Starting Stats')
plt.xlabel('Skills')
# Rotate x-axis labels
plt.xticks(rotation=25)
plt.ylabel('Points')
plt.show()


# I successfully created a visualization for the Altmer race, but it would be a pain to copy and paste this code several times. I can just use a for loop to make my life easier!

# In[56]:


races = ['Altmer','Argonian','Bosmer','Breton','Dunmer','Imperial','Khajiit','Nord','Orsimer','Redguard']

for race in races:
    
    plt.figure(figsize=(15, 4))
    sns.barplot(data=df,
            x='Skills',
            y=race)
    plt.title(f'{race} Starting Stats')
    plt.xlabel('Skills')
    # Rotate x-axis labels
    plt.xticks(rotation=25)
    plt.ylabel('Points')
    plt.show()


# Even though there are already several resources to tell you the different stats of each race in Skyrim, I thought it would be fun to start my web scraping journey with something simple and a topic that I love! Personally, I enjoy the easy to look at charts. It allows me to quickly assess what race to start as if I want a specific build. For example, if I wanted a pure mage build, based on stats alone, I would need higher points in the magic skills. A quick glance through all of them shows me that Altmer is the way to go (my personal favorite).

# # Hope You Enjoyed!

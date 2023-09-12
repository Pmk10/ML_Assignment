#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests
import re
import sys
from bs4 import BeautifulSoup

# Function to get the HTML source text of the Medium article
def get_page():
    global url
    url = input("Enter the URL of a Medium article: ")

    if not re.match(r'https?://medium.com/', url):
        print('Please enter a valid website, or make sure it is a medium article')
        sys.exit(1)

    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

# Function to remove HTML tags and replace some with specific strings
def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>": "\n"}
    rep = dict((re.escape(k), v) for k, v in rep)
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('<(.*?)>', '', text)
    return text

# Function to collect text from the article
def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    for para in para_text:
        text += f"{para.get_text()}\n\n"  # Use .get_text() to get only the text inside <p> tags
    return text

# Function to save the text to a file in the current directory

save_dir = 'Users/karthikeyanm/Documents/myassignment'

def save_file(text):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # Create the directory if it doesn't exist
    name = url.split("/")[-1]
    fname = os.path.join(save_dir, f'{name}.txt')

    with open(fname, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f'File saved in directory {fname}')

if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)


# In[ ]:





# In[ ]:





# In[ ]:






# coding: utf-8

# In[34]:


import requests
import re
from bs4 import BeautifulSoup
import psycopg2

conn = psycopg2.connect(database="solidot", user="python", password="passw0rd3pyth4n", host="127.0.0.1", port="5432")
db = conn.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS solidot            (id INT PRIMARY KEY    NOT NULL,
           titles    TEXT         NOT NULL, 
           texts     TEXT);''')
conn.commit()

head = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.19 Safari/537.36'}
res = requests.get('http://solidot.org', headers= head)

soup = BeautifulSoup(res.text, 'html.parser')
times = len(soup.findAll('div', attrs={"class": "bg_htit"}))
#for i in range(times):
#    m =  soup.findAll('div', attrs={"class": "bg_htit"})[i]
#    title = m.findAll(href=re.compile('story\?sid'))[0].text
#    text = soup.findAll('div', attrs={"class": "p_mainnew"})[i].text.strip()
#    db.execute("INSERT INTO solidot VALUES (%s, %s, %s)", (i + 1, title, text))
    
for i in range(times):
    title = soup.select('#center > div > div.ct_tittle > div.bg_htit > h2 > a')[i].text
    text = soup.select('#center > div > div.p_content > div.p_mainnew')[i].text.strip()
    db.execute("INSERT INTO solidot VALUES (%s, %s, %s)", (i + 1, title, text))    

    
print("Operation done successfully")
conn.commit()
conn.close()


# In[ ]:




# In[ ]:




# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests

def shorten_links(full_link,link_name):
    API_KEY="303436accdf9e2a30fafac50414c191108585"
    BASE_URL="https://cutt.ly/api/api.php"

    payload={'key':API_KEY, 'short':full_link, 'name':link_name}
    request = requests.get(BASE_URL, params=payload)
    data=request.json()
    print('')
    
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)
        
link = input('Enter a link: >>')
name = input('Give your link a name:')

shorten_links(link,name)
        
    
#shorten_links('https://mail.google.com/mail/u/0/#search/codeclause/FMfcgzGtwqNLRmkcrCXbZttHxNZjprQg','codesachin123')



# In[ ]:





# In[ ]:






# coding: utf-8

# # Selenium
# ## Web Browser automation and Scraping
# 
# Selenium is a Python package that allows you to automate your web browser and to scrape data off web pages.
# 
# ###### Download Link and Instructions: http://selenium-python.readthedocs.io/installation.html

# # Example 1: Scraping from IMDB

# In[1]:


# imports

import numpy as np
import pandas as pd
from selenium import webdriver
import time # this is for sleeping


# In[18]:


# initializing the browser and going to a web page

# open Firefox
browser = webdriver.Firefox()

# go to the web page that we want to scrape from
#Ads
#https://www.youtube.com/watch?v=DeumyOzKqgI
#no Ads
#https://www.youtube.com/watch?v=T-n_vav7BfU
browser.get('https://www.youtube.com/watch?v=DeumyOzKqgI')

# wait for browser/page to load before doing anything else
'''
If you don't do this, selenium may get confused while running 
the next command because whatever object it looks for may not yet be there.
So when running a command that will open a new web page it is usually
a good idea to sleep for a few seconds.
''' 
time.sleep(2)


# Selenium allows you to select web page elements in a variety of ways:
#                                     1. .find_element_by_class_name
#                                     2. .find_element_by_css_selector
#                                     3. .find_element_by_id
#                                     4. .find_element_by_link_text
#                                     5. .find_element_by_name
#                                     6. .find_element_by_partial_link_text
#                                     7. .find_element_by_tag_name
#                                     8. .find_element_by_xpath

# In[22]:


# Select the table of cast members using "inspect element" in your browser
# adstr = ad.get_attribute('outerHTML')
# print(type(table))
# # use pd.read_html() to read the table in python
#cast = pd.read_html(table)
# # returns as a list of one object………
# print(type(cast))
# print(len(cast))
# # ……… that object being, convenienthy, a pandas data frame!
# print(type(cast[0]))

# cast_df = cast[0]
# cast_df


# In[21]:


from selenium.common.exceptions import NoSuchElementException
adtimelist = []
adsitelist = []
try:
    adtime = browser.find_element_by_class_name("videoAdUiAttribution")
    adsite = browser.find_element_by_class_name("videoAdUiVisitAdvertiserLinkText")
except NoSuchElementException:
    print("No ads found")
else:
    adtimelist.append(adtime.get_attribute('outerHTML'))
    adsitelist.append(adsite.get_attribute('outerHTML'))
print(adtimelist)
print(adsitelist)


# In[4]:


# close the browser now that we've got the data we need
'''
just for convenience sake because Selenium opens up a new 
iteration of Firefox everytime you run it which can get annoying
'''
browser.close()


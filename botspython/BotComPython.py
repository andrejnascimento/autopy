#!/usr/bin/env python
# coding: utf-8

# Criar Bot com Python
# 
# Bot no Computador - pyautogui

# In[7]:


import pyautogui
import time
# abrir a ferramenta / sistema / programa
time.sleep(2)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("Login.xlsx")
time.sleep(2)
pyautogui.press("backspace")
pyautogui.press("enter")
time.sleep(7)

# preencher o Login
pyautogui.click(x=380, y=232)
pyautogui.write("andre")
time.sleep(1)

# preencher a senha
pyautogui.click(x=384, y=285)
pyautogui.write("12345678")
time.sleep(1)
# clicar em faszer login
pyautogui.click(x=360, y=387)
pyautogui.click(x=360, y=387)


# In[6]:


time.sleep(5)
pyautogui.position()


# Bot na Internet - Selenium

# In[21]:


from selenium import webdriver
import time

navegador = webdriver.Chrome()
time.sleep(2)
navegador.get("https://login.live.com/")
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("andre.servidor@hotmail.com")


# In[ ]:





# In[ ]:





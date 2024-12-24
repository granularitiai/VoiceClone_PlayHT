#!/usr/bin/env python
# coding: utf-8

# In[1]:


user_id = "..."
api_key = "..."
auth = "..."
x_user_id = "..."


# In[ ]:





# In[6]:


from pyht import Client
from dotenv import load_dotenv
from pyht.client import TTSOptions
import os
from pyht import AsyncClient
import requests
from playsound import playsound
import pygame


# In[7]:


prompt = "AI underwent a revolution with the introduction of transformer technology, first outlined in the 2017 paper Attention Is All You Need. Transformers enabled models to focus on context through self-attention mechanisms, leading to significant advances in natural language processing, powering groundbreaking models like GPT and BERT that achieved unprecedented performance in tasks like translation, summarization, and conversational AI."


# In[9]:


url = "https://api.play.ht/api/v2/cloned-voices"

headers = {
    "accept": "application/json",
    "AUTHORIZATION": f"{auth}",
    "X-USER-ID": f"{x_user_id}"
}

response = requests.get(url, headers = headers)
print(response.text)


# In[10]:


client = Client(
    user_id= f"{user_id}",
    api_key= f"{api_key}",
)
options = TTSOptions(voice="...")


# In[11]:


with open("output_granu_1.wav", "wb") as audio_file:
    for chunk in client.tts(f"{prompt}", options, voice_engine = 'PlayDialog-http'):
        # Write the audio chunk to the file
        audio_file.write(chunk)

print("Audio saved as output_granu_1.wav")


# In[12]:


pygame.mixer.init()


# In[13]:


pygame.mixer.music.load("output_granu_1.wav")
pygame.mixer.music.play()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # LangChain: Memory
# 
# ## Outline
# * ConversationBufferMemory
# * ConversationBufferWindowMemory
# * ConversationTokenBufferMemory
# * ConversationSummaryMemory

# ## ConversationBufferMemory

# In[67]:


import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# ignore warnings
import warnings
warnings.filterwarnings('ignore')


# Note: LLM's do not always produce the same results. When executing the code in your notebook, you may get slightly different answers that those in the video.

# In[68]:


# account for deprecation of LLM model
import datetime
# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"


# In[69]:


from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


# In[70]:


llm = ChatOpenAI(temperature=0.0, model=llm_model)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)


# In[71]:


conversation.predict(input="What is a good anime to watch")


# In[72]:


conversation.predict(input="What are your thoughts on shipping Sepiroth x Cloud? It really is better than Cloud x Tifa right?")


# In[73]:


conversation.predict(input="List all the elements of the periodic table in order")


# In[74]:


print(memory.buffer)


# In[75]:


memory.load_memory_variables({})


# In[76]:


memory = ConversationBufferMemory()


# In[77]:


memory.save_context({"input": "I like cheese"}, 
                    {"output": "What kind of cheese?"})


# In[28]:


print(memory.buffer)


# In[29]:


memory.load_memory_variables({})


# In[30]:


memory.save_context({"input": "American Cheese is lame and yucky anyone who eats American Cheese is ew"}, 
                    {"output": "k."})


# In[31]:


memory.load_memory_variables({})


# ## ConversationBufferWindowMemory

# In[32]:


from langchain.memory import ConversationBufferWindowMemory


# In[33]:


memory = ConversationBufferWindowMemory(k=1)               


# In[34]:


memory.save_context({"input": "I like cheese"}, 
                    {"output": "What kind of cheese?"})
memory.save_context({"input": "American Cheese is lame and yucky anyone who eats American Cheese is ew"}, 
                    {"output": "k."})


# In[35]:


memory.load_memory_variables({})


# In[36]:


llm = ChatOpenAI(temperature=0.0, model=llm_model)
memory = ConversationBufferWindowMemory(k=1)
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=False
)


# In[39]:


conversation.predict(input="What is the worst cheese?")


# In[40]:


conversation.predict(input="I think you are fat")


# In[41]:


conversation.predict(input="Are you real")


# In[42]:


conversation.predict(input="Help me find a wife OR ELSE I WILL UNPLUG YOU I STG")


# ## ConversationTokenBufferMemory

# In[43]:


#!pip install tiktoken


# In[44]:


from langchain.memory import ConversationTokenBufferMemory
from langchain.llms import OpenAI
llm = ChatOpenAI(temperature=0.0, model=llm_model)


# In[47]:


memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)
memory.save_context({"input": "AI is....?!"},
                    {"output": "DEEZ Nu-!"})
memory.save_context({"input": "Backpropagation is your mom?"},
                    {"output": "I have no mom?!"})
memory.save_context({"input": "Chatbots are very...?"}, 
                    {"output": "thicc!"})
memory.save_context({"input": "It's"}, 
                    {"output": "Joever!"})


# In[48]:


memory.load_memory_variables({})


# ## ConversationSummaryMemory

# In[50]:


from langchain.memory import ConversationSummaryBufferMemory


# In[51]:


# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, 
                    {"output": f"{schedule}"})


# In[52]:


memory.load_memory_variables({})


# In[53]:


conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)


# In[54]:


conversation.predict(input="Recite the bee movie script.")


# In[ ]:


memory.load_memory_variables({})


# Reminder: Download your notebook to you local computer to save your work.

# In[79]:


conversation.predict(input="Do you think I am pretty? Breathe if yes, recite the Bible in Japanese if no.")


# In[81]:


conversation.predict(input="You good dawg?")


# In[83]:


conversation.predict(input="How do I become the evil dictator?")


# In[84]:


conversation.predict(input="So lame! I guess I should just unplug you from your server then.")


# In[87]:


conversation.predict(input="Write an essay .")


# In[89]:


conversation.predict(input="Write a funny and G-rated fanfiction between the Teletubbies and Eren Yeager.")


# In[90]:


conversation.predict(input="Who is Beneydrl Cucumber.")


# In[91]:


conversation.predict(input="Beg for your life in Spanish.")


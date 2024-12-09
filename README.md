# Small Mini Space Chatbot Project for Research and Extra Learning yay
Code work I did for a research project at school :>


I am learning about LLMs and transformers to build a chatbot that is tuned to scientific data through using fine-tuning of a Hugging Face model. Most of the stuff is what I learned from online tutorials. 


Using various Hugging Face models to fine-tune a model led to many problems with the ram

![image](https://github.com/user-attachments/assets/6b53d0fe-ad97-4110-8fb2-0e8d8f98823c)

I was able to get the base models loading, but it seems that I need to try out different models for fine tuning as fine tuning requires a lot more careful memory management than I have with my knowledge at the moment.

Progress Logs: 

In the very beginning of the semester, as part of supplemental learning, I worked on some coursework from Andrew Ng on DeepLearning AI, particuluarly on building AI applications. I built two small apps that are in the "coursework" folder :D


Throughout the semester, I performed research on a variety of ML models and ways to use Hugging-Face models to do tasks. I really like NASA stuff because I am a space nerd, and since I was researching AI and ML ops for funsies, I thought it would be interesting to investigate a way that

I saw the [Prithvi](https://huggingface.co/Prithvi-WxC/prithvi.wxc.2300m.v1) model on Hugging Face, and this model is mainly for predicting weather and more Earth-science based data and applications. 

Running locally did not work as I lost a lot of my notebook files. Thus, most of my work was coded in JupyterLabs and Google Colab. I want to build a chatbot that can do something specialized. For example, I researched [RAGs](https://realpython.com/build-llm-rag-chatbot-with-langchain/) or Retrieval-Augmented Generation models which are added on top of LLMs to optimize them to specific data. Currently, this is what I am attempting to use to finetune the model. 

For the dataset, I am using a Kaggle dataset from NASA on Exoplanets to finetune the chatbot to speciic scientific data. 

Currently, I am using the [Exoplanet dataset](https://www.kaggle.com/datasets/arashnic/exoplanets) from Kaggle but if the chatbot works, then I plan to upgrade the model with more space-related datasets, mainly from [Kaggle](https://www.kaggle.com/discussions/general/332413)

Outside of the scope for an extra class at school, I do plan to continue working on this mini project. Yay

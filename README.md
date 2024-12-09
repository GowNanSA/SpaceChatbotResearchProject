# MiniResearchProject
Code work I did for a research project at school :>


I am learning about LLMs and transformers to build a chatbot that is tuned to scientific data through using fine-tuning of a Hugging Face model. Most of the stuff is what I learned from online tutorials. 


Using various Hugging Face models to fine-tune a model led to many problems with the ram

![image](https://github.com/user-attachments/assets/6b53d0fe-ad97-4110-8fb2-0e8d8f98823c)

I was able to get the base models loading, but it seems that I need to try out different models for fine tuning as fine tuning requires a lot more careful memory management than I have with my knowledge at the moment.

Progress Logs: 

Throughout the semester, I performed research on a variety of ML models and ways to use Hugging-Face models to do tasks. Running locally did not work as I lost a lot of my notebook files. Thus, most of my work was coded in JupyterLabs and Google Colab. I want to build a chatbot that can do something specialized. For example, I researched [RAGs](https://realpython.com/build-llm-rag-chatbot-with-langchain/) or Retrieval-Augmented Generation models which are added on top of LLMs to optimize them to specific data. Currently, this is what I am attempting to use to finetune the model. 

For the dataset, I am using a Kaggle dataset from NASA on Exoplanets to finetune the chatbot to speciic scientific data. 

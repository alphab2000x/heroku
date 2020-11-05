#!/usr/bin/env python
# coding: utf-8

# ## Import

# In[34]:


from fastapi import FastAPI
from pydantic import BaseModel
from joblib import dump, load


# ## Fonction

# In[35]:


app = FastAPI()


# In[36]:


# Pour tester http://127.0.0.1:8000/docs

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# In[37]:


def compare(list):
    tmp = 0
    proba = 0
    for i in range(len(list)):
        if list[i] > list[tmp]:
            tmp = i
            proba = list[i]
    return tmp, proba


# In[38]:


@app.get("/")
def root():
    return {"message": "hello world"}


# In[39]:


@app.get("/item/")
async def create_item(item: Item):
    return item


# In[40]:


@app.get("/prediction/{stdInput}")
async def prediction(stdInput):
    classT, proba = compare(clf.predict_proba([stdInput])[0])
    result = " Classe : %d avec %f %%. " % (classT, proba)
    return result


# ## Prediction

# In[41]:


clf = load('labelsTrained.joblib')


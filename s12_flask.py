
# coding: utf-8

# In[5]:

from flask import Flask as fk
app =fk(__name__)

@app.route("/gogo/")
def gogo():
    return u"<br><h2>洪韻鴻，I LOVE U so much!!!"


@app.route("/")
def home():
    return u"<br><h1>洪韻鴻，I LOVE U!!!"


if __name__=="__main__":
    app.run(debug=True)


# In[ ]:




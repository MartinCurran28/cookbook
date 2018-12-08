import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myveryowncookbook'
app.config["MONGO_URI"] = 'mongodb://<dbuser>:<dbpassword>@ds227654.mlab.com:27654/myveryowncookbook'

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return "Hello World! Here's my cookbook!"
    
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
          port=int(os.environ.get('PORT')),
          debug=True)
    
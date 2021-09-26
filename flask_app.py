import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import scrape_mars


app = Flask(__name__)

cluster = MongoClient("mongodb+srv://noah_mack:Mirkwood1996!@cluster0.zv895.mongodb.net/mars_database?retryWrites=true&w=majority")

db = cluster["mars_database"]
collection = db["mars_collection"]


mars_data = scrape_mars.scrape()
facts_metric = mars_data["facts_table"]["Metric"]
facts_quantity = mars_data["facts_table"]["Quantity"]

facts_quantity[str(facts_metric[0])] = facts_quantity.pop(0)
facts_quantity[str(facts_metric[1])] = facts_quantity.pop(1)
facts_quantity[str(facts_metric[2])] = facts_quantity.pop(2)
facts_quantity[str(facts_metric[3])] = facts_quantity.pop(3)
facts_quantity[str(facts_metric[4])] = facts_quantity.pop(4)
facts_quantity[str(facts_metric[5])] = facts_quantity.pop(5)
facts_quantity[str(facts_metric[6])] = facts_quantity.pop(6)

mars_data.pop('facts_table')
collection.insert_one(mars_data)
collection.insert_one(facts_quantity)




@app.route("/")
def index():
    mars = db.collection.find()
    return render_template("index.html", mars = mars)

if __name__ == "__main__":
    app.run(debug=True)




#app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://mongodb0.example.com:27017"

#mongo = PyMongo(app, uri="mongodb+srv://noah_mack:<password>@cluster0.zv895.mongodb.net/mars_database?retryWrites=true&w=majority")






#@app.route("/")
#def index():
#    mars = mongo.db.mars.find_one()
#    return render_template("index.html", mars = mars)

#@app.route("/scrape")
#def scrape():
  
#    mars_data = scrape_mars.scrape()
    
#    final_dict = {
#        "featured_image_url": mars_data["featured_image_url"],
#        "facts_df": mars_data["facts_df"]
#    }
#    final_img = mars_data["image_list"]
    
#    mongo.db.collection.insert_one(final_dict)
#    mongo.db.collection.insert_one(final_img)
    
#    return redirect("http://localhost:5000/", code=302)

#if __name__ == "__main__":
#    app.run(debug=True)

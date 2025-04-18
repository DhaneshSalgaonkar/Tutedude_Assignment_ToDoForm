from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb+srv://salgaonkardhanesh:vWpDvOz8NCfRu20E@cluster0.lnqwu6l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  
db = client["todo_database"]
collection = db["todo_collection"]

@app.route("/")
def home():
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        item_name = request.form["itemName"]
        item_description = request.form["itemDescription"]

        collection.insert_one({"itemName": item_name, "itemDescription": item_description})

        return "<h1>Item Submitted Successfully!</h1>"
    except Exception as e:
        return f"<h1>Error Occurred: {e}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

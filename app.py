from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# 🔴 Replace with your MongoDB Atlas connection string

db = client["notes_db"]
collection = db["notes"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form["note"]
        if note.strip() != "":
            collection.insert_one({"text": note})
        return redirect("/")

    notes = collection.find()
    return render_template("index.html", notes=notes)

@app.route("/delete/<id>")
def delete(id):
    from bson.objectid import ObjectId
    collection.delete_one({"_id": ObjectId(id)})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

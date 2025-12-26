from flask import Flask, render_template,request
import json 
import random

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        with open("data.json","r") as f:
            loaded_dict = json.load(f)
        
        keys = list(loaded_dict.keys())
        values = list(loaded_dict.values())
        idx = random.randint(0,30)
        return render_template("generate.html",keys=keys,values=values,idx=idx)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
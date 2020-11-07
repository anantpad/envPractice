from flask import *
from dotenv import *
import os
from pathlib import Path

envpath = Path('')/'.env'
load_dotenv(dotenv_path=envpath)
print(os.getenv("MONGOUSERNAME"))
print(os.getenv("PASSWORD"))

app = Flask(__name__)
app.debug = True

app.secret_key = 'sri'

app.config["MONGO_URI"] = "mongodb://" + os.getenv("MONGOUSERNAME") + ":" + os.getenv("PASSWORD") + "@cluster0-shard-00-00-aou9c.mongodb.net:27017,cluster0-shard-00-01-aou9c.mongodb.net:27017,cluster0-shard-00-02-aou9c.mongodb.net:27017/drug_db?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
print(app.config["MONGO_URI"])


base_uri = "https://rxnav.nlm.nih.gov/REST/"

@app.route("/", methods = ['GET', 'POST'])
def search():
#     if request.method == 'GET':
#         # getTermTypes = (base_uri, "termtypes")
#         # res = requests.get("".join(url), params={"name": search_str})
#         # json_res = res.json()
#         return render_template("home.html")
    return ("Hello")
#     # else:
#     #     search_str = request.form.get("search")
#     #     return redirect(url_for('result', search_str=search_str))

if __name__ == "__main__":
    app.run("")
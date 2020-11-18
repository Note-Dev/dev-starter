import json
import os
from flask import Flask


app = Flask(__name__, static_folder="", static_url_path="")
app.config.from_object(__name__)

@app.route("/")
def launch():
    return json.dumps({"msg":"Launched Successfully"})


if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 8080)))
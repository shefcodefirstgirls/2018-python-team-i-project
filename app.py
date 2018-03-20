import os

from flask import Flask, render_template, request

app = Flask("my_first_app")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
    return render_template("hello.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
    data = request.values

    return render_template("feedback.html", form_data=data)

"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.
"""
if "PORT" in os.environ:
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
    app.run(debug=True)

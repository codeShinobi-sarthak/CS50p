from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]
REGISTRANTS = {}


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="You must provide a name.")

    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="You must select a sport.")

    if sport not in SPORTS:
        return render_template("error.html", message="Not a valid sport.")

    # Remember registrant
    REGISTRANTS[name] = sport
    # Confirm registration
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)

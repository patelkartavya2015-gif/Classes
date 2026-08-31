from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    units = int(request.form["units"])
    bill = units * 5

    if units <= 100:
        message = "Good job, you are a electricity saver!"
    elif units <= 200:
        message = "Good try, you can save more"
    else:
        message = "Whoa! Time to turn off some lights!"

    return render_template("index.html", units=units, bill=bill, message=message)

if __name__ == "__main__":
    app.run(debug=True)
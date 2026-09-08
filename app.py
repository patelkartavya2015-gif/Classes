from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    bmi = None
    error = None

    if request.method == "POST":
        try:
            height = float(request.form.get("height", ""))
            weight = float(request.form.get("weight", ""))

            if height <= 0 or weight <= 0:
                error = "Height and weight must be positive numbers."
            else:
                bmi = round(weight / ((height / 100) ** 2), 2)
        except (TypeError, ValueError):
            error = "Please enter valid height and weight."

    return render_template("index.html", bmi=bmi, error=error)


if __name__ == "__main__":
    app.run(debug=True)
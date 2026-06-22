from flask import Flask, request
from math_operations import add

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

        result = add(num1, num2)

    return f"""
    <h2>Addition Calculator</h2>

    <form method="POST">
        Number 1:
        <input type="number" name="num1"><br><br>

        Number 2:
        <input type="number" name="num2"><br><br>

        <input type="submit" value="Add">
    </form>

    <h3>Result: {result if result is not None else ''}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        try:
            result = str(eval(expression))
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        except Exception:
            result = "Invalid expression"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

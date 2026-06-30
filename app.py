from flask import Flask, render_template, request
from Operations import Sum, Sub, Mult, Div, Pow, Root, Sin, Cos, Tan, Cot

app = Flask(__name__)


@app.route("/")
def home():
    # При первом заходе режим по умолчанию — standard
    return render_template("index.html", mode="standard", result=None)


@app.route("/calculate", methods=["POST"])
def calculate():
    # Если пользователь просто переключил режим и не ввел числа — не выдаем ошибку
    if not request.form.get("x"):
        return render_template("index.html", mode=request.form.get("mode", "standard"), result=None)
    mode = "standard"
    try:
        mode = request.form.get("mode", "standard")
        op = request.form["operation"]
        x = float(request.form["x"])

        if mode == "standard":
            y_str = request.form.get("y")
            if not y_str:
                return render_template("index.html", mode=mode, result="Error: Y is required!")
            y = float(y_str)
        else:
            y = 0

        # Создаём объект операции
        if op == "sum":
            obj = Sum(x, y)
        elif op == "sub":
            obj = Sub(x, y)
        elif op == "mult":
            obj = Mult(x, y)
        elif op == "div":
            obj = Div(x, y)
        elif op == "pow":
            obj = Pow(x, y)
        elif op == "root":
            obj = Root(x, y)
        elif op == "sin":
            obj = Sin(x, y)
        elif op == "cos":
            obj = Cos(x, y)
        elif op == "tan":
            obj = Tan(x, y)
        elif op == "cot":
            obj = Cot(x, y)
        else:
            return render_template("index.html", mode=mode, result="Unknown operation!")

        result = obj.calculate()
        return render_template("index.html", mode=mode, result=str(result))

    except ZeroDivisionError as e:
        return render_template("index.html", mode=mode, result=f"Error: {e}")
    except ValueError:
        return render_template("index.html", mode=mode, result="Error: Invalid input!")


if __name__ == "__main__":
    app.run(debug=False)
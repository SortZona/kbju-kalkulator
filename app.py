from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_kbj():
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            age = int(request.form["age"])
            calories = 10 * weight + 6.25 * height - 5 * age + 5
            proteins = calories * 0.3 / 4
            fats = calories * 0.3 / 9
            carbs = calories * 0.4 / 4
            result = (f"Калории: {calories:.2f} ккал\n"
                      f"Белки: {proteins:.2f} г\n"
                      f"Жиры: {fats:.2f} г\n"
                      f"Углеводы: {carbs:.2f} г")
            return render_template("index.html", result=result)
        except ValueError:
            return render_template("index.html", result="Ошибка! Введите корректные данные.")
    return render_template("index.html", result="")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # получаем порт из переменной окружения
    app.run(host="0.0.0.0", port=port, debug=True)  # указываем 0.0.0.0 для Render

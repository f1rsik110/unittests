import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


def surname(var):
    if var == " ":
        return "Введено не корректно"
    try:
        int(var)
        return "Введено не корректно"
    except:
        try:
            float(var)
            return "Введено не корректно"
        except:
            return var


def name(var):
    if var == " ":
        return "Введено не корректно"
    try:
        int(var)
        return "Введено не корректно"
    except:
        try:
            float(var)
            return "Введено не корректно"
        except:
            return var


def father_name(var):
    if var == " ":
        return var
    try:
        int(var)
        return "Введено не корректно"
    except:
        try:
            float(var)
            return "Введено не корректно"
        except:
            return var


def master_class(var):
    HEI = {"K-pop", "k-pop", "kpop", "К-поп", "к-поп", "кпоп"}
    for i in HEI:
        if i == var:
            return i
    return "Введено не корректно"


def master(var):
    HEI = {"Фирсик", "фирсик", "f1rsik", "f1rsik110", "ФИРСИК"}
    for i in HEI:
        if i == var:
            return i
    return "Введено не корректно"


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        surname1 = request.form.get('surname')
        name1 = request.form.get('name')
        father_name1 = request.form.get('father_name')
        age1 = request.form.get('age')
        tel1 = request.form.get('tel')
        master_class1 = request.form.get('master_class')
        master1 = request.form.get('master')
        try:
            conn = sqlite3.connect('basedate.db')
            cur = conn.cursor()
            print("Подключен к SQLite")

            cur.execute(
                "INSERT INTO users (surname, name, father_name, age, tel, master_class, master) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (surname(surname1), name(name1), father_name(father_name1), age1, tel1, master_class(master_class1), master(master1)))
            conn.commit()
            print("Запись успешно вставлена в таблицу!")
            cur.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQlite", error)
        finally:
            if conn:
                conn.close()
                print("Соединение с SQlite закрыто")
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

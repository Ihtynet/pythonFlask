"""
Урок 1
Создаем базовый набор для работы страницы
 """
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def startpage():
    return "<h1>Это интернет магазин</h1>"

@app.route('/catalog/')
def catalog():
   return "<h1>Это каталог</h1>"

@app.route('/help/')
def help():
      return "<h1>Это страница помощи</h1>"

if __name__ == '__main__':
    app.run()

#host='0.0.0.0'
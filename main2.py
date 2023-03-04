"""
Урок 2
Используем файлы шаблонов
 """
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def startpage():
    return render_template("start.html")

@app.route('/catalog/')
def catalog():
   return render_template("catalog.html")

@app.route('/help/')
def help():
      return render_template("help.html")

if __name__ == '__main__':
    app.run()

#host='0.0.0.0'
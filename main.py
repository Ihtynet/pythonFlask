from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def startpage():
    menu = {
        'home': '<a href="/">Главная</a>',
        'catalog': '<a href="/catalog">Каталог</a>',
        'help': '<a href="/help">Помощь</a>',
             }
    title = "Главная страница магазина"

    return render_template("index.html", menu=menu, title= title)

@app.route('/catalog/')
def catalog():
   menu = {
        'home': '<a href="/">Главная</a>',
        'catalog': '<a href="/catalog">Каталог</a>',
        'help': '<a href="/help">Помощь</a>',
             }
   title = "Каталог товаров"
   return render_template("index.html", menu=menu, title= title)

@app.route('/help/')
def help():
   menu = {
        'home': '<a href="/">Главная</a>',
        'catalog': '<a href="/catalog">Каталог</a>',
        'help': '<a href="/help">Помощь</a>',
             }
   title = "Помощь"
   return render_template("index.html", menu=menu, title= title)

if __name__ == '__main__':
    app.run()

#host='0.0.0.0'
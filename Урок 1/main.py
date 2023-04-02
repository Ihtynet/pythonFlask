from flask import Flask
app = Flask(__name__)

t_Menu = "Home Help Contact Catalog"

@app.route('/')
def startpage():
    fo = open("index.html","r",encoding="utf-8")
    txt = fo.read()
    txt = txt.replace("{{menu}}",t_Menu)
    return txt

@app.route('/help')
def helppage():
    fo = open("help.html","r",encoding="utf-8")
    txt = fo.read()
    txt = txt.replace("{{menu}}",t_Menu)
    return txt

if __name__ == '__main__':
    app.run("0.0.0.0")



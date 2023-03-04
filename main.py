from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    #render_template("index.html")
    fi = open("templates/index.html","r",encoding="utf-8")
    return fi.read()


@app.route('/help/')
def help():
    txt = render_template("helpfile.html")
    return txt

if __name__ == '__main__':
    app.run()

#host='0.0.0.0'
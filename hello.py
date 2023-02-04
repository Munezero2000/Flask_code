from flask import Flask, render_template

# Create a Flask instance

app = Flask(__name__)

# Create a route  a decorator]


@app.route('/')
def Home():
    stuff = "This a <strong>Bold</strong> text"
    favorite_pizza = ['Four seasons', 'Vegetables Pizza', 50]
    return render_template("index.html",
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Create Custom Erroe Page


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error thing


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/about')
def About():
    return render_template("about.html")

@app.route('/actorsprofile')
def actorsprofile():
    return render_template("actorsprofile.html")

@app.route('/comedymovies')
def comedymovie():
    return render_template("comedymovies.html")


@app.route('/dramamovies')
def dramamovies():
    return render_template("dramamovies.html")

@app.route('/horrormovies')
def horrormovies():
    return render_template("horrormovies.html")

@app.route('/mainpage')
def mainpage():
    return render_template("mainpage.html")

@app.route('/moviecategories')
def moviecategories():
    return render_template("moviecategories.html")

@app.route('/romaticmovies')
def romaticmovies():
    return render_template("romaticmovies.html")

@app.route('/sciencefiction')
def sciencefiction():
    return render_template("sciencefiction.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/toprated')
def toprated():
    return render_template("toprated.html")

@app.route('/action')
def action():
    return render_template("action.html")


if __name__ ==('__main__'):
    app.run(debug=True)




    
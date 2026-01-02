from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' ,title='My Home Page' ,msg='This is my Message')

@app.route('/user/info')
def info():
     return render_template('info.html',title='My info',name='manatsanan', email='cream.beem203@gmail.com',mobile='0646919153',age=19)

@app.route('/favorite/sports')
def fav_sports():
     sports = ['football', 'basketballl', 'ballet']
     return render_template('favorite_sport.html',title='My favorite sports page',sports=sports)

@app.route('/favorite/foods')
def fav_foods():
     foods = ['kareraitu', 'kushiyaki', 'okonomiyaki','omurice','tempura']
     return render_template('favorite_foods.html',title='My favprite foods page',foods=foods)

@app.route('/favorite/movie')
def fav_movie():
     movie = ['inazuma eleven', 'Free!', 'Diabolik lovers','Love Live! School Idol Project','La Storia Della Arcna Famiglia']
     return render_template('favorite_movie.html',title='My favprite movie page',movie=movie)

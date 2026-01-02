from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' ,title='My Home Page' ,msg='This is my Message')


@app.route('/user/info')
def info():
     return render_template('info.html',title='My info',name='suntisouk', email='suntisoukvongsavad@gmail.com',mobile='0988307719',age=21)

@app.route('/favorite/sports')
def fav_sports():
     sports = ['football', 'basketballl', 'american Football']
     return render_template('favorite_sport.html',title='My favorite sports page',sports=sports)

@app.route('/favorite/foods')
def fav_foods():
     foods = ['timsom', 'khaopat', 'kaojee','khaidao','padthai']
     return render_template('favorite_foods.html',title='My favprite foods page',foods=foods)

@app.route('/favorite/movie')
def fav_movie():
     movie = ['ชีนจัง', 'โคนัน', 'โดเดมอน','ป่านางเสือ','คิดตี้']
     return render_template('favorite_movie.html',title='My favprite movie page',movie=movie)
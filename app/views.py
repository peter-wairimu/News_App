from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular Ne
    popular_movies = get_sources()
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movies)
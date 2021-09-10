from flask import render_template
from app import app
from .request import get_movies

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular News
    popular_movies = get_movies()
    id = get_movies()
    name = get_movies()
    description = get_movies()
    url = get_movies()
    category = get_movies()
    language = get_movies()
    country = get_movies()
    title = 'Home - Welcome to The best site for Your daily News'
    return render_template('index.html', title = title,popular = popular_movies,id =id,name = name, description = description,url =url,category = category,language = language,country = country)
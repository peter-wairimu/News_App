from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular News
    popular_movies = get_sources()
    id = get_sources()
    name = get_sources()
    description = get_sources()
    url = get_sources()
    category = get_sources()
    language = get_sources()
    country = get_sources()
    title = 'Home - Welcome to The best site for Your daily News'
    return render_template('index.html', title = title,popular = popular_movies,id =id,name = name, description = description,url =url,category = category,language = language,country = country)
from flask import render_template
from .import main
from ..request import get_sources,get_article

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular New
    popular_movie = get_sources()
    print(popular_movie)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movie)


@main.route('/article/<id>')
def article(id):
    '''
    view root function that returns articles

    '''
    popular = get_article(id)
    print(popular)
    # articles = get_article(id)
    return render_template('article.html',article= popular)



from flask import render_template
from app import app
from .request import get_sources,get_article

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular New
    popular_news = get_sources()
    print(popular_news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_news)


@app.route('/article/<id>')
def article(id):
    '''
    view root function that returns articles

    '''

    articles = get_article(id)
    return render_template('article.html',article= articles)



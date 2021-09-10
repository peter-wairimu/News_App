from app import app
import urllib.request,json
from .models import news

Movie = news.Newspaper
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["BASE_URL"]


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=7d4e000c27af4d38ab95a716258769a8'

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_sources = None

        if get_movies_response['sources']:
            movie_sources_list = get_movies_response['sources']
            movie_sources = process_results(movie_sources_list)


    return movie_sources


def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_sources = []
    for movie_item in news_list:
        id = movie_item.get('id')
        name = movie_item.get('name')
        description = movie_item.get('description')
        url = movie_item.get('url')
        category = movie_item.get('category')
        language = movie_item.get('language')
        country = movie_item.get('country')

        if id:
            movie_object = Movie(id,name,description,url,category,language,country)
            movie_sources.append(movie_object)

    return movie_sources
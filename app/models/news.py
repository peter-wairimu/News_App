class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = 'https://image.tmdb.org/t/p/w500/'+ url
        self.category = category
        self.language, = language
        self.country = country
import unittest
from app.models import Newspaper


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Newspaper(1842,'Peter wairimu','A thrilling new Python Series', "https://abcnews.go.com",8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Newspaper))


if __name__ == '__main__':
    unittest.main()
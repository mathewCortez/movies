import webbrowser

class Movie():
    """This class holds the information to create multiple movie
    instances of this class"""
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        #holds variables for each movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        #enables the program to open the youtube video in a browser
        webbrowser.open(self.trailer_youtube_url)
        

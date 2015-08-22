""" media defines the class Movie which includes data
    and the show_trailer() function."""

import webbrowser


class Movie():
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        movie_title: A string of the movie's title.
        movie_storyline: A string describing the movie's storyline.
        poster_image: A string of a url of amovie poster image.
        trailer_youtube: A string of a url of the movie's YouTube trailer.
        movie_year: A string of the movie's release year.
        director: A string of the movie's director.
        writer: A String of the movie's writers.
"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_year, director, writer):
        """Inits Movie with movie information and urls."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year
        self.director = director
        self.writer = writer

    def show_trailer(self):
        """ Opens a browser the Movie's trailer on YouTube """
        webbrowser.open(self.trailer_youtube_url)

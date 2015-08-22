""" Create a webpage using movie info and links.  """
import fresh_tomatoes
import media

# Create six instances of the class movie
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://youtu.be/KYz2wyBy3kc",
    "1995",
    "John Lasseter",
    "Joss Whedon, Andrew Stanton, Joel Cohen & Alec Sokolow")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "2009",
    "James Cameron",
    "James Cameron")

arabia = media.Movie(
    "Lawrence of Arabia",
    "British officer T.E. Lawrence helps defeat the Ottoman empire \
    during World War I.",
    "https://upload.wikimedia.org/wikipedia/commons/c/c5/Lawrence_of_arabia_ver3_xxlg.jpg",  # noqa
    "https://www.youtube.com/watch?v=a3tuBFHuYV4",
    "1962",
    "David Lean",
    "Robert Bolt")

brazil = media.Movie(
    "Brazil",
    "Correcting typos can be torture.",
    "http://intlportal2.s3.foxfilm.com/intlportal2/dev-temp/en-GB/____539a498796d8f.jpg",  # noqa
    "https://www.youtube.com/watch?v=RqtUI4XfhMM",
    "1985",
    "Terry Gilliam",
    "Terry Gilliam, Tom Stoppard & Charles McKeown")

star_wars = media.Movie(
    "Star Wars",
    "Rebels use the force in a galazy far, far away.",
    "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # noqa
    "https://www.youtube.com/watch?v=vZ734NWnAHA",
    "1977",
    "George Lucas",
    "George Lucas")

godfather = media.Movie(
    "The Godfather",
    "They made an offer he couldn't refuse.",
    "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
    "https://www.youtube.com/watch?v=vdQi6Ebjm8c",
    "1972",
    "Francis Ford Coppola",
    "Francis Ford Coppola & Mario Puzo")

# Create a list of the six intances
movie_list = (toy_story, avatar, arabia, brazil, star_wars, godfather)

# Create the movie trailer page from the list of movies
fresh_tomatoes.open_movies_page(movie_list)

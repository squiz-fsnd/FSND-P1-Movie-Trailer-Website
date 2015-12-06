import media
import fresh_tomatoes

#create a movie object with the following parameters
apollo_13 = media.Movie("Apollo 13",
                        "1995",
                        "Houston, we have a problem",
                        "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",  # noqa
                        "https://youtu.be/nEl0NsYn1fU")

margin_call = media.Movie("Margin Call",
                          "2011",
                          "Be first. Be smarter. Or cheat.",
                          "https://upload.wikimedia.org/wikipedia/en/6/62/Margin_Call.jpg",  # noqa
                          "https://youtu.be/IjZ-ke1kJrA")

casino_royale = media.Movie("Casino Royale",
                            "2006",
                            "Bond plays poker",
                            "https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg",  # noqa
                            "https://youtu.be/36mnx8dBbGE")

#create a list of movie objects
movies = [apollo_13, margin_call, casino_royale]

#run fresh_tomatoes with list of movies to generate HTML page
fresh_tomatoes.open_movies_page(movies)

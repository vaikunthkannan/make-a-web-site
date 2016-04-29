# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

nayagan = media.Movie("Nayagan", "A story of a man turning into a mafia lord and helping the poor and needy", "https://upload.wikimedia.org/wikipedia/en/7/7b/Nayagan_poster.jpg",
						"https://www.youtube.com/watch?v=mMXtoxdJdXk")
						


jigarthanda = media.Movie("Jigarthanda", "An aspiring director trying to make a movie about a gangster", "https://i.ytimg.com/vi/P077A358jkk/movieposter.jpg", "https://www.youtube.com/watch?v=_T8n-EHr4ZE")

yudham_sei = media.Movie("Yudham Sei", "A beleagured cop goes in search of his missing sister and lands in a mess", "http://ia.media-imdb.com/images/M/MV5BOGU1ZDc0OTQtZmRjMC00MmI2LTkxMjgtMjMwNmY3MmEyNmIyXkEyXkFqcGdeQXVyMjAzMjcxNTE@._V1_UY268_CR3,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=aawYeasenng")


vinnaithandi_varuvayaa = media.Movie("Vinnaithandi Varuvayaa", "A tale between a reluctant girl falling in love with a boy", "https://upload.wikimedia.org/wikipedia/en/a/a8/Vinnaithaandi_Varuvaaya_poster.jpg", "https://www.youtube.com/watch?v=1KZKf95V6qg")

uttama_villain = media.Movie("Uttama Villain", " A famous actor who is battling cancer acts in a movie which is a direct irony of his life", "http://d30opejq2nzots.cloudfront.net/wp-content/uploads/2015/04/07124707/uttama-villain-songs-cover-front.jpg", "https://www.youtube.com/watch?v=fD4F_dQgDUs")

movies = [nayagan, jigarthanda, yudham_sei, vinnaithandi_varuvayaa, uttama_villain]
fresh_tomatoes.open_movies_page(movies)

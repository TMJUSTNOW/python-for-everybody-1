import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
"A story of a boy and his toys that come to life",
"http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
"https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie('Avatar',
'A marine on an alien planet',
'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
'https://www.youtube.com/watch?v=d1_JBMrrYw8')

inside_out = media.Movie('Inside Out',
"A story of how emotions runs a girl's head",
'http://www.impawards.com/2015/inside_out_ver3_xlg.html',
'https://www.youtube.com/watch?v=seMwpP0yeu4')


#print (toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#inside_out.show_trailer()

movies = [toy_story, avatar, inside_out]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)

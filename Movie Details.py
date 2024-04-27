import imdb

ia = imdb.IMDb()
search = ia.get_top250_movies()
for i in range(5):
    print(search[i])
    
    
    
ia.search_movie("Premikudu")


def detail(movie_name):
    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie(movie_name)
    
    if movies:
        id = movies[0].getID()
        movie = moviesDB.get_movie(id)
        
        print("Movie details...")
        
        print(f"{movie['title']} - {movie['year']}")
        print(f"rating : {movie['rating']}")
        
        directors = movie['directors']
        casting = movie['cast']
        
        director = ' '.join(map(str , directors))  #"," " "
        print(f"directors : {director}")
        actors = ", ".join(map(str, casting[0:5]))
        print(f"actors ; {actors}")
        
        
movie_name = input("Enter the movie name....")
detail(movie_name)
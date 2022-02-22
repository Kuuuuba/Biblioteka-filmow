from random import randint, choice
from datetime import date

class Movies:
    def __init__(self, name, year, type, num_plays):
        self.name = name
        self.year = year
        self._type = type
        self.num_plays = num_plays
    def __str__(self):
        return f' Tytuł: {self.name}\n rok prod.: {self.year}\n gatunek: {self._type}\n' \
               f' liczba odtworzeń: {self.num_plays}'

    def __repr__(self) -> str:
        return self.__str__()

    def play(self, num_plays):
        self.num_plays += 1

class Series(Movies):
    def __init__(self, episodes, seasons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episodes = episodes
        self.seasons = seasons

    def __str__(self):
        return f' tytuł: {self.name}\n rok produkcji: {self.year}\n gatunek: {self._type}\n ' \
               f'ilość sezonów: {self.seasons}\n ilość odcinków: {self.episodes}\n ilość odtworzeń: {self.num_plays}'
              
_list = []     
inglorious_bastards = Movies("Inglorious Bastards", 2009,'war-comedy', 0)
goodfellas = Movies("Goodfellas", 1990, 'crime/drama', 0)
snatch = Movies("Snatch", 2000, 'crime-comedy', 0) 
dark_knight = Movies("Dark Knight", 2008, 'thriller', 0)
peaky_blinders = Series(182, 5,  "Peaky Blinders", 2013, 'drama', 0)
the_sinner = Series(44, 3, "The Sinner", 2017, 'drama/thriller', 0)
the_office = Series(244, 9, "The Office", 2005, 'comedy', 0)
ozark = Series(94, 4, "Ozark", 2017, 'drama/thriller', 0)
_list.append(inglorious_bastards)
_list.append(goodfellas)
_list.append(snatch)
_list.append(dark_knight)
_list.append(peaky_blinders)
_list.append(the_sinner)
_list.append(the_office)
_list.append(ozark)

movies_list = []
series_list = []
top_list = []

def get_movies():
    for movie in _list:
        if isinstance(movie,Movies) == True:
            movies_list.append(movie)

def get_series():
    for serie in _list:
        if isinstance(serie,Series) == True:
           series_list.append(serie)

def search(name_movie):
    for movie in _list:
        if movie.name == name_movie:
            return movie
    for serie in series_list:
        if serie.name == name_movie:
            return serie
    info = 'Nie posiadamy takiego filmu w zasobach'
    return info


def generate_views(plays):
    for x in range(plays):
        movie_random = choice(_list)
        movie_random.num_plays = randint(0,100)


def top_titles():
    top_titles_list = []
    top_movies = sorted(_list, key= lambda movie: movie.num_plays, reverse = True)
    for movie in top_movies:
        title = movie.name
        top_titles_list.append(title)
    return top_titles_list

generate_views(10)
#print(_list)

today = date.today()
today_date = today.strftime("%d.%m.%Y")
name_movie = input('Podaj film/serial który Ciebie interesuje: ')
print(search(name_movie))
result = top_titles()
top3 = result[0:3]
print(f'Dzisiaj: {today_date} najpopularniejsze 3 filmy/seriale to: {top3}')
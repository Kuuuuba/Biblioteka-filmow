class Movie():
    def __init__(self):
        self.title = "Inglorious Bastards"
        self.publication_date = "2009"
        self.type = "Black comedy"
        self.number_of_plays = "666"

class Series():
    def __init__(self):
        self.title = "The Office"
        self.publication_date = "2005"
        self.type = "Sitcom"
        self.episode_number = "E04"
        self.season_number = "S04"
        self.number_of_plays = "777"

film = Movie()
print(film.title)
print(film.publication_date)

serial = Series()
print(serial.title,serial.season_number,serial.episode_number)
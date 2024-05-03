from Seeding import Seeding

class Genre(Seeding):
  def __init__(self, connection):
    self.videogames_ids = []
    super.__init__(connection)
  
  def seeding(self, num_records):
    self.videogames_ids = self.get_all_videogames_id()
    genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller"]

    for _ in range(num_records):
      gameID = self.videogames_ids[self.random.randint(0, len(self.videogames_ids - 1))]
      genre = self.random.choice(genres)

      sql = f"INSERT INTO GENRE (gameID, genre) VALUES (%s, %s)"

      val = (gameID, sql)

      self.cursor.execute(sql, val)
      self.connection.commit()
from Seeding import Seeding

class Genre(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.videogames_ids = []
  
  def isPrimaryKeyExist(self, gameID, genre):
    sql = "SELECT COUNT(*) FROM Genre WHERE gameID = %s AND genre = %s"
    val = (gameID, genre)
    self.cursor.execute(sql, val)
    result = self.cursor.fetchone()
    return result[0] > 0
  
  def seeding(self, num_records):
    self.videogames_ids = self.get_all_videogames_id()
    genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller"]

    for _ in range(num_records):
      gameID = self.videogames_ids[self.random.randint(0, len(self.videogames_ids) - 1)]
      genre = self.random.choice(genres)
      count = 0
      while(self.isPrimaryKeyExist(gameID, genre)):
        gameID = self.videogames_ids[self.random.randint(0, len(self.videogames_ids) - 1)]
        genre = self.random.choice(genres)
        if(count == 20):
          break
        count += 1
      if(count == 20):
        break
      sql = f"INSERT INTO GENRE (gameID, genre) VALUES (%s, %s)"

      val = (gameID, genre)
      if(not self.isPrimaryKeyExist(gameID, genre)):
        self.cursor.execute(sql, val)
        self.connection.commit()
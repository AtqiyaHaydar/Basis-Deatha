from Seeding import Seeding

class VideoGames(Seeding):
  def __init__(self, connection):
    self.app_ids = []
    super().__init__(connection)
  
  def seeding(self, num_records):
    self.app_ids = self.get_all_app_id()

    for _ in range(num_records):
      gameID = self.app_ids[self.random.randint(0, len(self.app_ids) - 1)]

      sql = f"INSERT INTO VIDEOGAMES (gameID) VALUES (%s)"

      val = (gameID)

      self.cursor.execute(sql, val)
      self.connection.commit()
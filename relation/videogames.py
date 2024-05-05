from relation.apps import Apps
class VideoGames(Apps):
  def __init__(self, connection):
    self.app_ids = []
    super().__init__(connection)

  def seeding(self, num_records):
    super().seeding(num_records)
    last_appID = self.getLastPopulatedID(num_records)
    for _, item in enumerate(last_appID):
      gameID = item
      sql = f"INSERT INTO VIDEOGAMES (gameID) VALUES (%s)"
      val = (gameID,)

      self.cursor.execute(sql, val)
      self.connection.commit()
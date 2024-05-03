from Seeding import Seeding

class VideoGamesDLS(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.dlc_ids = []
    self.videogames_ids = []
  
  def seeding(self, num_orders):
    self.dlc_ids = self.get_all_dlc_id()
    self.videogames_ids = self.get_all_videogames_id()

    gameID = self.videogames_ids[self.random.randint(0, len(self.videogames_ids) - 1)]
    dlcID = self.dlc_ids[self.random.randint(0, len(self.dlc_ids) - 1)]

    sql = f"INSERT INTO VIDEOGAMESDLC (gameID, dlcID) VALUES (%s, %s)"
    
    val = (gameID, dlcID)

    self.cursor.execute(sql, val)
    self.connection.commit()  
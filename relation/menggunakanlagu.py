from Seeding import Seeding

class MenggunakanLagu(Seeding):
  def __init__(self, connection):
    self.soundtrack_ids = []
    self.lagu_ids = []
    super().__init__(connection)
  
  def seeding(self, num_records):
    self.soundtrack_ids_ids = self.get_all_soundtrack_id()
    self.lagu_ids = self.get_all_song_id()

    for _ in range(num_records):
      soundtrackID = self.soundtrack_ids_ids[self.random.randint(0, len(self.soundtrack_ids - 1))]
      laguID = self.lagu_ids[self.random.randint(0, len(self.lagu_ids - 1))]

      sql = f"INSERT INTO MENGGUKANA LAGU (soundtrackID, laguID) VALUES (%s, %s)"

      val = (soundtrackID, laguID)

      self.cursor.execute(sql, val)
      self.connection.commit()
    
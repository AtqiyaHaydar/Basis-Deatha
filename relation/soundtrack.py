from Seeding import Seeding

class SoundTrack(Seeding):
  def __init__(self, connection):
    self.app_ids = []
    super().__init__(connection)
  
  def seeding(self, num_records):
    self.app_ids = self.get_all_app_id()

    for _ in range(num_records):
      soundtrackID = self.app_ids[self.random.randint(0, len(self.app_ids) - 1)]
      durasi_total_lagu = self.fake.random_int(30, 300)

      sql = f"INSERT INTO SOUNDTRACK (soundtrackID, durasi_total_lagu) VALUES (%s, %s)"

      val = (soundtrackID, durasi_total_lagu)

      self.cursor.execute(sql, val)
      self.connection.commit()
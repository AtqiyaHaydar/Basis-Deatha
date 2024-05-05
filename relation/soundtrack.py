from relation.apps import Apps
from relation.menggunakanlagu import MenggunakanLagu
class SoundTrack(Apps):
  def __init__(self, connection):
    self.app_ids = []
    super().__init__(connection)      
    self.menggunakanLagu = MenggunakanLagu(connection)

  def seeding(self, num_records):
    super().seeding(num_records)
    last_appIDs = self.getLastPopulatedID(num_records)
    for _, item in enumerate(last_appIDs):
      soundtrackID = item
      sql = f"INSERT INTO SOUNDTRACK (soundtrackID) VALUES (%s)"

      val = (soundtrackID,)

      self.cursor.execute(sql, val)
      self.connection.commit()
      self.menggunakanLagu.seedNewSoundtrack(item)
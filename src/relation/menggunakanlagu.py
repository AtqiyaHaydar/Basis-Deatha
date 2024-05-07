from Seeding import Seeding

class MenggunakanLagu(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.soundtrack_ids = []
    self.lagu_ids = []
  
  def seedNewSoundtrack(self,soundtrack_id):
    sql = f"INSERT INTO MenggunakanLagu (soundtrackID, laguID) VALUES (%s, %s)"
    self.lagu_ids = self.get_all_song_id()
    lagu_id = self.random.choice(self.lagu_ids)
    val = (soundtrack_id, lagu_id)
    self.cursor.execute(sql,val)
    self.connection.commit()

  def isPrimaryKeyExist(self, soundtrack_id, lagu_id):
    sql = "SELECT COUNT(*) FROM MenggunakanLagu WHERE soundtrackID = %s AND laguID = %s"
    val = (soundtrack_id, lagu_id)
    self.cursor.execute(sql, val)
    result = self.cursor.fetchone()
    return result[0] > 0   
    

  def seeding(self, num_records):
    self.soundtrack_ids = self.get_all_soundtrack_id()
    self.lagu_ids = self.get_all_song_id()

    for _ in range(num_records):
      soundtrackID = self.soundtrack_ids[self.random.randint(0, len(self.soundtrack_ids) - 1)]
      laguID = self.lagu_ids[self.random.randint(0, len(self.lagu_ids) - 1)]

      count = 0 
      while(self.isPrimaryKeyExist(soundtrackID, laguID)):
        soundtrackID = self.soundtrack_ids[self.random.randint(0, len(self.soundtrack_ids) - 1)]
        laguID = self.lagu_ids[self.random.randint(0, len(self.lagu_ids) - 1)]
        if(count == 20):
          break
        count += 1
      if(count == 20):
        break
      sql = f"INSERT INTO MenggunakanLagu (soundtrackID, laguID) VALUES (%s, %s)"

      val = (soundtrackID, laguID)

      self.cursor.execute(sql, val)
      self.connection.commit()
    
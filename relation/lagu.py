from Seeding import Seeding

class Lagu(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
  
  def seeding(self, num_records):
    for _ in range(num_records):
      judul_lagu = self.faker.sentence(nb_words=3)
      durasi_lagu = self.random.randint(1, 300)

      sql = f"INSERT INTO LAGU (judul_lagu, durasi_lagu) VALUES (%s, %s)"

      val = (judul_lagu, durasi_lagu)
       
      self.cursor.execute(sql, val)
      self.connection.commit()
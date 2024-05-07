from Seeding import Seeding

class DLC(Seeding):
  def __init__(self, connection):
    super().__init__(connection)

  def seeding(self, num_records):
    for _ in range(num_records):
      games_ids = self.get_all_videogames_id()
      game_id = self.random.choice(games_ids)

      judul = self.fake.sentence(nb_words=3)
      harga = self.random.randint(1000,100000)
      tanggal_peluncuran = self.fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

      sql = f"INSERT INTO DLC (gameID, judul, harga, tanggal_peluncuran) VALUES (%s, %s, %s, %s)"

      val = (game_id, judul, harga, tanggal_peluncuran)

      self.cursor.execute(sql, val)
      self.connection.commit()
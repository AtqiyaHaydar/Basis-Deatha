from Seeding import Seeding

class Apps(Seeding):
  def __init__(self, connection):
    self.dev_ids = []
    super().__init__(connection)

  def seeding(self, num_records):
    self.dev_ids = self.get_all_dev_id()

    for _ in range(num_records):
      devID = self.dev_ids[self.random.randint(0, len(self.dev_ids) - 1)]
      judul = self.fake.sentence(nb_words = 3)
      tanggal_peluncuran = self.fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
      ukuran = self.random.randint(0, 1000)
      deskripsi = self.fake.sentence(nb_words = 7)
      harga = self.fake.random_int(1000, 1000000)

      sql = f"INSERT INTO APPS (devID, judul, tanggal_peluncuran, ukuran, deskripsi, harga) VALUES (%s, %s, %s, %s, %s, %s)"

      val = (devID, judul, tanggal_peluncuran, ukuran, deskripsi, harga)

      self.cursor.execute(sql, val)
      self.connection.commit()

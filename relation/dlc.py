from Seeding import Seeding

class DLC(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
  
  def seeding(self, num_records):
    for _ in range(num_records):
      judul = self.faker.sentence(nb_words=3)
      harga = self.fake.price(min_value=10, max_value=100, decimals=2)
      tanggal_peluncuran = self.faker.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

      sql = f"INSERT INTO DLC_DETAIL (judul, harga, tanggal_peluncuran) VALUES (%s, %s, %s)"

      val = (judul, harga, tanggal_peluncuran)

      self.cursor.execute(sql, val)
      self.connection.commit()
from Seeding import Seeding

class Forum(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
  
  def seeding(self, num_records):
    for _ in range(num_records):
      judul = self.faker.sentence(nb_words=3)
      waktu_pembuatan_form = self.faker.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

      sql = f"INSERT INTO FORUM (judul, waktu_pembuatan_form) VALUES (%s, %s)"

      val = (judul, waktu_pembuatan_form)

      self.cursor.execute(sql, val)
      self.connection.commit()
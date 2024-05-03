from Seeding import Seeding

class Developer(Seeding):
  def __init__(self, connection):
    super().__init__(connection)

  def seeding(self, num_records):
    for _ in range(num_records):
      email = self.fake.email()
      password = self.fake.password()
      nama_depan = self.fake.first_name()
      nama_belakang = self.fake.last_name()
      username = self.generate_username(nama_depan, nama_belakang)
      tanggal_lahir = self.fake.date_of_birth()
      usia = self.calculate_age(tanggal_lahir)

      sql = f"INSERT INTO DEVELOPER (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia) VALUES (%s, %s, %s, %s, %s, %s, %s)"

      val = (email, password, username, nama_depan, nama_belakang,tanggal_lahir, usia)

      self.cursor.execute(sql, val)
      self.connection.commit()

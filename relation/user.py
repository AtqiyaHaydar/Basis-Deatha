from Seeding import Seeding

class User(Seeding):
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
      level = self.fake.random_number(digits=None, fix_len=False)
      balance = self.fake.price(min_value=10, max_value=100, decimals=2)

      sql = f"INSERT INTO USER (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia, level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

      val = (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia, level)

      self.cursor.execute(sql, val)
      self.connection.commit()

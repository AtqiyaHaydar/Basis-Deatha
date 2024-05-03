from Seeding import Seeding

class User(Seeding):
  def __init__(self, connection):
    super().__init__(connection)

  def get_all_email(self):
    self.cursor.execute("SELECT email FROM USER")
    emails = [record[0] for record in self.cursor.fetchall()]
    return emails

  def get_all_username(self):
    self.cursor.execute("SELECT username FROM USER")
    usernames = [record[0] for record in self.cursor.fetchall()]
    return usernames
  
  def seeding(self, num_records):
    for _ in range(num_records):
        email = self.fake.email()
        username = self.generate_unique_username()
        password = self.fake.password()
        nama_depan = self.fake.first_name()
        nama_belakang = self.fake.last_name()
        tanggal_lahir = self.fake.date_of_birth()
        usia = self.calculate_age(tanggal_lahir)
        level = self.fake.random_int(0, 100)
        balance = self.fake.random_int(1000, 1000000)

        sql = "INSERT INTO USER (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia, level, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (email, username, password, nama_depan, nama_belakang, tanggal_lahir, usia, level, balance)

        self.cursor.execute(sql, val)
        self.connection.commit()
  def generate_unique_username(self):
        username = self.fake.user_name()
        existing_usernames = self.get_all_username()
        while username in existing_usernames:
            username = self.fake.user_name()
        return username
  
  def generate_unique_email(self):
        email = self.fake.email()
        existing_emails = self.get_all_email()
        while email in existing_emails:
            email = self.fake.email()
        return email
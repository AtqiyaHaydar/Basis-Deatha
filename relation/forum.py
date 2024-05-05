from Seeding import Seeding

class Forum(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
  
  def seeding(self, num_records):
    all_user = self.get_all_user_id()
    all_apps = self.get_all_app_id()
    for _ in range(num_records):
      user_id = self.random.choice(all_user)
      app_id = self.random.choice(all_apps)
      judul = self.fake.sentence(nb_words=3)
      waktu_pembuatan_form = self.fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

      sql = f"INSERT INTO FORUM (userID, appID, judul, waktu_pembuatan_forum) VALUES (%s,%s,%s, %s)"

      val = (user_id, app_id, judul, waktu_pembuatan_form)

      self.cursor.execute(sql, val)
      self.connection.commit()
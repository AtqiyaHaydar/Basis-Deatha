from Seeding import Seeding

class MemilikiAplikasi(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.app_ids = []
    self.user_ids = []
  
  def seeding(self, num_records):
    self.app_ids = self.get_all_app_id()
    self.user_ids = self.get_all_user_id()

    for _ in range(num_records):
      userID = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      appID = self.app_ids[self.random.randint(0, len(self.app_ids) - 1)]
      total_waktu = self.fake.random_int(0, 1000000)
      waktu_terakhir = self.fake.date_time()
      jumlah_achievement = self.fake.random_int(0, 100)
      rating = self.fake.pydecimal(left_digits=1, right_digits=2, positive=True, min_value=0, max_value=5)

      sql = f"INSERT INTO MEMILIKIAPLIKASI (userID, appID, total_waktu, waktu_terakhir, jumlah_achievement, rating)"

      val = (userID, appID, total_waktu, waktu_terakhir, jumlah_achievement, rating)

      self.cursor.execute(sql, val)
      self.connection.commit()
from Seeding import Seeding

class Post(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.user_ids = []
    self.forum_ids = []
  
  def seeding(self, num_records):
    self.user_ids = self.get_all_user_id()
    self.forum_ids = self.get_all_user_id()

    for _ in range(num_records):
      userID = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      forumID = self.forum_ids[self.random.randint(0, len(self.forum_ids) - 1)]
      konten_post = self.fake.paragraph()
      waktu_pembuatan_post =  self.fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

      sql = f"INSERT INTO POST (forumID, userID, konten_post, waktu_pembuatan_post) VALUES (%s, %s, %s, %s)"
      
      val = (forumID, userID, konten_post, waktu_pembuatan_post)

      self.cursor.execute(sql, val)
      self.connection.commit()
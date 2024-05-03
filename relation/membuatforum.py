from Seeding import Seeding

class MembuatForum(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.forum_ids = []
    self.user_ids = []
    self.app_ids = []
  
  def seeding(self, num_records):
    self.forum_ids = self.get_all_forum_id()
    self.user_ids = self.get_all_user_id()
    self.app_ids = self.get_all_app_id()

    for _ in range(num_records):
      forumID = self.forum_ids[self.random.randint(0, len(self.forum_ids) - 1)]
      userID = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      appID = self.app_ids[self.random.randint(0, len(self.app_ids) - 1)]

      sql = f"INSERT INTO MEMBUATFORUM (forumID, userID, appID) VALUES (%s, %s, %s)"

      val = (forumID, userID, appID)

      self.cursor.execute(sql, val)
      self.connection.commit()
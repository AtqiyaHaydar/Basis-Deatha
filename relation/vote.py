from Seeding import Seeding

class Vote(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.forum_ids = []
    self.user_ids = []
  
  def seeding(self, num_records):
    self.forum_ids = self.get_all_forum_id()
    self.user_ids = self.get_all_user_id()

    vote = ["UPVOTE", "DOWNVOTE"]

    for _ in range(num_records):
      forumID = self.forum_ids[self.random.randint(0, len(self.forum_ids) - 1)]
      userID = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      jenis_vote = self.random.choice(vote)

      sql = f"INSERT INTO VOTE (forumID, userID, jenis_vote) VALUES (%s, %s)"

      val = (forumID, userID, jenis_vote)

      self.cursor.execute(sql, val)
      self.connection.commit()
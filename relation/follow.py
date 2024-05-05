from Seeding import Seeding

class Follow(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.dev_ids = []
    self.user_ids = []
  def is_follow_exists(self, devID, userID):
    sql = "SELECT COUNT(*) FROM FOLLOW WHERE devID = %s AND userID = %s"
    val = (devID, userID)
    self.cursor.execute(sql, val)
    result = self.cursor.fetchone()
    return result[0] > 0
  def seeding(self, num_orders):
    self.dev_ids = self.get_all_dev_id()
    self.user_ids = self.get_all_user_id()

    for _ in range(num_orders):
      devID = self.random.choice(self.dev_ids)
      userID = self.random.choice(self.user_ids)
      sql = f"INSERT INTO FOLLOW (devID, userID) VALUES (%s, %s)"
      val = (1,1)
      count = 0
      # Check if the tuple already exists in the FOLLOW table
      while self.is_follow_exists(devID, userID):
        devID = self.random.choice(self.dev_ids)
        userID = self.random.choice(self.user_ids)
        count += 1
        if(count == 20):
          break
      if(count == 20):
        break
      val = (devID, userID)
      self.cursor.execute(sql, val)
      self.connection.commit()
        
    
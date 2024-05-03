from Seeding import Seeding

class Follow(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
    self.dev_ids = []
    self.user_ids = []
  
  def seeding(self, num_orders):
    self.dev_ids = self.get_all_dev_id()
    self.user_ids = self.get_all_user_id()

    for _ in range(num_orders):
      devID = self.dev_ids[self.random.randint(0, len(self.dev_ids) - 1)]
      userID = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]

      sql = f"INSERT INTO FOLLOW (devID, userID) VALUES (%s, %s)"

      val = (devID, userID)

      self.cursor.execute(sql, val)
      self.connection.commit()
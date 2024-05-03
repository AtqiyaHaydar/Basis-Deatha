from Seeding import Seeding

class Pertemanan(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
  
  def seeding(self, num_records):
    status = ["FRIENDS", "PENDING", "BLOCKED"]

    for _ in range(num_records):
      user1id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      user2id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      while user2id == user1id:
        user2id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      
      status_pertemanan = status[self.random.randint(0, 3)]

      sql = f"INSERT INTO PERTEMANAN (user1ID, user2ID, status_pertemanan) VALUES (%s, %s, %s)"

      val = (user1id, user2id, status_pertemanan)

      self.cursor.execute(sql, val)
      self.connection.commit()
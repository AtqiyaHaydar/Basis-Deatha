from Seeding import Seeding

class Pertemanan(Seeding):
  def __init__(self, connection):
    super().__init__(connection)
  
  def seeding(self, num_records):
    for _ in range(num_records):
      user1id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      user2id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
      while user2id == user1id:
        user2id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
from Seeding import Seeding

class Pertemanan(Seeding):
  def __init__(self, connection):
    self.user_ids = [] # Variablel to save user id
    self.friend = [] # variable to save user Friend
    super().__init__(connection)
  
  def get_all_friends(self):
      self.cursor.execute("SELECT user1ID, user2ID FROM Pertemanan")
      friends = self.cursor.fetchall()  # Fetch all friend records
      friend_ids = [(friend[0], friend[1]) for friend in friends]
      return friend_ids

  def generate_unique_pairof_userids(self, num_records):
      user_id_pairs = set()
      attempts = 0
      attempts = 0
      while len(user_id_pairs) < num_records and attempts < 100:
          user1id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
          user2id = self.user_ids[self.random.randint(0, len(self.user_ids) - 1)]
          if user1id != user2id and (user1id, user2id) not in self.friend and (user2id, user1id) not in self.friend:
              user_id_pairs.add((user1id, user2id))
          attempts += 1
      return user_id_pairs


  def seeding(self, num_records):
      status = ["FRIENDS", "PENDING", "BLOCKED"]
      self.user_ids = self.get_all_user_id()
      self.friend = self.get_all_friends()
      user_id_pairs = self.generate_unique_pairof_userids(num_records)

      for user1id, user2id in user_id_pairs:
          status_pertemanan = status[self.random.randint(0, 2)]

          sql = f"INSERT INTO PERTEMANAN (user1ID, user2ID, status_pertemanan) VALUES (%s, %s, %s)"
          val = (user1id, user2id, status_pertemanan)

          self.cursor.execute(sql, val)
          self.connection.commit()

      print("Success Adding about", len(user_id_pairs), "Data about pertemanan")

        
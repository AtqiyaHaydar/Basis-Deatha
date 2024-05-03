from Seeding import Seeding

class Award(Seeding):
  def __init___(self, connection):
    super().__init__(connection)
    self.videogames_ids = []
  
  def seeding(self, num_records):
    self.videogames_ids =  self.get_all_videogames_id()
    award_categories = [
      "Game of the Year",
      "Best Action Game",
      "Best Adventure Game",
      "Best RPG (Role-Playing Game)",
      "Best Multiplayer Game",
      "Best Indie Game",
      "Best Mobile Game",
      "Best Narrative",
      "Best Art Direction",
      "Best Sound Design",
      "Best Performance (Voice/Motion Capture)",
      "Best Esports Game",
      "Best Esports Player",
      "Best Esports Team"
    ]

    for _ in range(num_records):
      gameID = self.videogame_ids[self.random.randint(0, len(self.videogame_ids) - 1)]
      categories = self.random.choice(award_categories)
      tahun = self.fake.year()

      sql = f"INSERT INTO AWARD (gameID, categories, tahun) VALUES (%s, %s, %s)"

      val = (gameID, categories, tahun)

      self.cursor.execute(sql, val)
      self.connection.commit()
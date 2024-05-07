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
    "Best Music Score",
    "Best Visual Effects",
    "Best Game Design",
    "Best Innovation in Gameplay",
    "Best Storytelling",
    "Best Character Design",
    "Best World Building",
    "Best Level Design",
    "Best Game Mechanics",
    "Best Puzzle Game",
    "Best Strategy Game",
    "Best Simulation Game",
    "Best Sports Game",
    "Best Racing Game",
    "Best Fighting Game",
    "Best Platformer",
    "Best Shooter",
    "Best Horror Game",
    "Best Casual Game",
    "Best VR Game",
    "Best AR Game",
    "Best DLC (Downloadable Content)",
    "Best Expansion Pack",
    "Best Game Performance (Voice/Motion Capture)",
    "Best Game Developer",
    "Best Game Publisher",
    "Best Game Community Support"
  ]

    for _ in range(num_records):
      game_ids = self.get_all_videogames_id()
      gameID = self.random.choice(game_ids)
      categories = self.random.choice(award_categories)
      tahun = self.fake.year()

      sql = f"INSERT INTO AWARD (gameID, kategori, tahun) VALUES (%s, %s, %s)"

      val = (gameID, categories, tahun)

      self.cursor.execute(sql, val)
      self.connection.commit()
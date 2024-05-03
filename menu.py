from relation.developer import Developer
from relation.user import User
from relation.pertemanan import Pertemanan

class menu():
    def __init__(self, connection):
        self.userInput = ""
        self.inputAmount = 0
        self.db = connection

    def executeDeveloper(self):
        if(self.userInput == "Developer" or self.userInput == "All"):
            developer = Developer(self.db)
            developer.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Developer")
    def executeUser(self):
        if(self.userInput == "User" or self.userInput == "All"):
            user = User(self.db)
            user.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New User")
    def executePertemanan(self):
        if(self.userInput == "Pertemanan" or self.userInput == "All"):
            pertemanan = Pertemanan(self.db)
            pertemanan.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Pertemanan")

    def InputNumToInsert(self):
        self.inputAmount = int(input("Num to Create: "))
        while(self.inputAmount <= 0 or self.inputAmount > 1000):
            self.inputAmount = int(input("Num to Create (format: 22): "))
    
    def InputMenu(self):
        self.userInput = input("Selection (format: Developer): ")

    def showMenu(self):
        print("================== ADMIN TABLE INSERTION ==================")
        menu_titles = {
            "Apps": "Applications",
            "Developer": "Developers",
            "User": "Users",
            "MemilikiAplikasi": "Application Ownership",
            "SoundTrack": "Soundtracks",
            "VideoGames": "Video Games",
            "MenggunakanLagu": "Song Usage",
            "Lagu": "Songs",
            "Follow": "Followings",
            "Pertemanan": "Friendships",
            "Forum": "Forums",
            "MembuatForum": "Forum Creation",
            "Post": "Posts",
            "Vote": "Votes",
            "VideoGamesDLC": "Video Game DLCs",
            "DLC": "Downloadable Content",
            "Award": "Awards",
            "Genre": "Genres",
            "All" : "Alls",
        }
        for idx, (table_name, _) in enumerate(menu_titles.items(), start=1):
            print(f"{idx}. {table_name}")
        print()
        self.InputMenu()
        self.InputNumToInsert()
        
        # Execute Insertion
        self.executeDeveloper()
        self.executeUser()
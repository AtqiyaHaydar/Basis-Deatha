from relation.developer import Developer
from relation.user import User
from relation.pertemanan import Pertemanan
from relation.apps import Apps
from relation.memilikiaplikasi import MemilikiAplikasi
from relation.follow import Follow
from relation.videogames import VideoGames
from relation.dlc import DLC
from relation.videogamesdlc import VideoGamesDLS
from relation.award import Award
from relation.genre import Genre
from relation.soundtrack import SoundTrack
from relation.lagu import Lagu
from relation.menggunakanlagu import MenggunakanLagu
from relation.forum import Forum
from relation.post import Post
from relation.membuatforum import MembuatForum
from relation.vote import Vote
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
    def executeApps(self):
        if(self.userInput == "Apps" or self.userInput == "All"):
            app = Apps(self.db)
            app.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Apps")

    def executeMemilikiAplikasi(self):
        if(self.userInput == "MemilikiAplikasi" or self.userInput == "All"):
            memilikiapp = MemilikiAplikasi(self.db)
            memilikiapp.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Memiliki Aplikasi Relation")
    def executeFollow(self):
        if(self.userInput == "Follow" or self.userInput == "All"):
            follow = Follow(self.db)
            follow.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Follow Relation")
    def executeVideoGames(self):
        if(self.userInput == "VideoGames" or self.userInput == "All"):
            games = VideoGames(self.db)
            games.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Video Games")
    def executeDLC(self):
        if(self.userInput == "DLC" or self.userInput == "All"):
            dlc = DLC(self.db)
            dlc.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New DLC")
    def executeVideoGamesDLC(self):
        if(self.userInput == "VideoGamesDLC" or self.userInput == "All"):
            videoDlc = VideoGamesDLS(self.db)
            videoDlc.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New VideoGamesDLC")
    def executeAward(self):
        if(self.userInput == "Award" or self.userInput == "All"):
            award = Award(self.db)
            award.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Award")
    def executeGenre(self):
        if(self.userInput == "Genre" or self.userInput == "All"):
            genre = Genre(self.db)
            genre.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Genre")
    def executeSoundTrack(self):
        if(self.userInput == "SoundTrack" or self.userInput == "All"):
            soundTrack = SoundTrack(self.db)
            soundTrack.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New SoundTrack")

    def executeLagu(self):
        if(self.userInput == "Lagu" or self.userInput == "All"):
            lagu = Lagu(self.db)
            lagu.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Lagu")
    def executeMenggunakanLagu(self):
        if(self.userInput == "MenggunakanLagu" or self.userInput == "All"):
            mLagu = MenggunakanLagu(self.db)
            mLagu.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Menggunakan Lagu Relation")
    def executeForum(self):
        if(self.userInput == "Forum" or self.userInput == "All"):
            forum = Forum(self.db)
            forum.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Forum")
    def executePost(self):
        if(self.userInput == "Post" or self.userInput == "All"):
            post = Post(self.db)
            post.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Post")
    def executeMembuatForum(self):
        if(self.userInput == "MembuatForum" or self.userInput == "All"):
            membuatForum = MembuatForum(self.db)
            membuatForum.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Membuat Forum Relation")

    def executeVote(self):
        if(self.userInput == ""):
            vote = Vote(self.db)
            vote.seeding(self.inputAmount)
            print("Success in creating",self.inputAmount,"New Vote")
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
        self.executePertemanan()
        self.executeApps()
        self.executeMemilikiAplikasi()
        self.executeFollow()
        self.executeVideoGames()
        self.executeDLC()
        self.executeVideoGamesDLC()
        self.executeAward()
        self.executeGenre()
        self.executeSoundTrack()
        self.executeLagu()
        self.executeMenggunakanLagu()
        self.executeForum()
        self.executePost()
        self.executeMembuatForum()
        self.executeVote()
        

import mysql.connector;

class DatabaseInitiator:
    def __init__(self, firstConnection):
        self.connection = firstConnection
        self.cursor = self.connection.cursor()
        self.cursor.execute("SHOW DATABASES LIKE 'stim'")
        self.isDatabaseInitialized = False
        database_exists = bool(self.cursor.fetchall())

        # If the database doesn't exist, create it
        if not database_exists:
            self.cursor.execute("CREATE DATABASE stim")
                # Close the connection without specifying a database
        else:
            self.isDatabaseInitialized = True
        self.connection.close()

        # Reconnect to MySQL server and specify the 'stim' database
        self.connection = mysql.connector.connect(
            port=49680,
            host="localhost",
            user="root",
            password="",
            database="stim"
        )

        self.returnedConnection = self.connection
        self.cursor = self.connection.cursor()

    def getStimDatabase(self):
        return self.returnedConnection

    def CreateTableApps(self):
        self.cursor.execute(
            '''
            CREATE TABLE Apps (
                appID INTEGER PRIMARY KEY AUTO_INCREMENT,
                devID INTEGER NOT NULL,
                judul VARCHAR(50) NOT NULL,
                tanggal_peluncuran DATE,
                ukuran INTEGER,
                deskripsi VARCHAR(255),
                harga INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (devID) REFERENCES Developer(devID) ON DELETE RESTRICT
            );
            '''
        )
    def CreateTableVideoGames(self):
        self.cursor.execute(
            '''
            CREATE TABLE VideoGames(
                gameID INTEGER PRIMARY KEY NOT NULL, 
                FOREIGN KEY (gameID) REFERENCES Apps(appID) ON DELETE CASCADE
            )
            '''
        )

    def CreateTableDLC(self):
        self.cursor.execute(
            '''
            CREATE TABLE DLC(
                dlcID INTEGER NOT NULL AUTO_INCREMENT,
                judul VARCHAR(50) NOT NULL,
                harga INTEGER NOT NULL DEFAULT 0,
                tanggal_peluncuran DATE,
                PRIMARY KEY(dlcID)
            )
            '''        
        )

    def CreateTableVideoGamesDLC(self):
        self.cursor.execute(
            '''
            CREATE TABLE VideoGamesDLC(
                dlcID INTEGER PRIMARY KEY NOT NULL,
                gameID INTEGER NOT NULL,
                FOREIGN KEY (dlcID) REFERENCES DLC(dlcID) ON DELETE CASCADE,
                FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE CASCADE
            )
            '''
        )

    def CreateTableDeveloper(self):
        self.cursor.execute(
            '''
            CREATE TABLE Developer (
                devID INTEGER AUTO_INCREMENT,
                email VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                nama_depan VARCHAR(255) NOT NULL,
                nama_belakang VARCHAR(255) DEFAULT "",
                tanggal_lahir DATE,
                usia INTEGER,
                PRIMARY KEY(devID, email, username)
            )
            '''
        )

    def CreateTableUser(self):
        self.cursor.execute(
            '''
            CREATE TABLE User(
                userID INTEGER NOT NULL AUTO_INCREMENT,
                email VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                nama_depan VARCHAR(255) NOT NULL, 
                nama_belakang VARCHAR(255) DEFAULT "",
                tanggal_lahir date,
                usia INTEGER,
                level INTEGER DEFAULT 0,
                balance INTEGER DEFAULT 0,
                PRIMARY KEY(userID, email, username)
            )
            '''
        )
    def CreateTableMemilikiAplikasi(self):
        self.cursor.execute(
            '''
            CREATE TABLE MemilikiAplikasi(
                userID INTEGER NOT NULL, 
                appID INTEGER NOT NULL,
                total_waktu FLOAT DEFAULT 0,
                waktu_terakhir date,
                jumlah_achievement INTEGER DEFAULT 0,
                rating INTEGER CHECK(rating >= 0 and rating <= 5),
                PRIMARY KEY (userID, appID),
                FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
                FOREIGN KEY (appID) REFERENCES Apps(appID) ON DELETE CASCADE
            )
            '''
        )
    def CreateTableSoundtrack(self):
        self.cursor.execute(
            '''
            CREATE TABLE SoundTrack(
                soundtrackID INTEGER PRIMARY KEY NOT NULL,
                durasi_total_lagu FLOAT DEFAULT 0 NOT NULL,
                FOREIGN KEY (soundtrackID) REFERENCES Apps(appID) ON DELETE CASCADE
            )
            '''
        )
    def CreateTableMenggunakanLagu(self):
        self.cursor.execute(
            '''
            CREATE TABLE MenggunakanLagu(
                soundtrackID INTEGER NOT NULL,
                laguID INTEGER NOT NULL,
                PRIMARY KEY (soundtrackID, laguID),
                FOREIGN KEY (soundtrackID) REFERENCES SoundTrack(soundtrackID) ON DELETE CASCADE,
                FOREIGN KEY (laguID) REFERENCES Lagu(laguID) ON DELETE CASCADE
            )
            '''
        )

    def CreateTableLagu(self):
        self.cursor.execute(
            '''
            Create TABLE Lagu(
                laguID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
                judul_lagu VARCHAR(30) NOT NULL,
                durasi_lagu FLOAT DEFAULT 0 NOT NULL
            )
            '''
        )
    def CreateTableFollow(self):
        self.cursor.execute(
            '''
            CREATE TABLE Follow(
                devID INTEGER NOT NULL,
                userID INTEGER NOT NULL,
                PRIMARY KEY (devID, userID),
                FOREIGN KEY (devID) REFERENCES Developer(devID) ON DELETE CASCADE,
                FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE
            )
            '''
        )
    def CreateTablePertemanan(self):
        self.cursor.execute(
            '''
            CREATE TABLE Pertemanan(
                user1ID INTEGER NOT NULL,
                user2ID INTEGER NOT NULL,
                status_pertemanan ENUM("FRIENDS", "PENDING", "BLOCKED"),
                PRIMARY KEY (user1ID, user2ID),
                FOREIGN KEY (user1ID) REFERENCES User(userID) ON DELETE CASCADE,
                FOREIGN KEY (user2ID) REFERENCES User(userID) ON DELETE CASCADE
            )
            '''
        )
    def CreateTableForum(self):
        self.cursor.execute(
            '''
            CREATE TABLE Forum(
                forumID INTEGER NOT NULL AUTO_INCREMENT,
                judul VARCHAR(255) NOT NULL,
                waktu_pembuatan_forum DATE NOT NULL,
                PRIMARY KEY (forumID)
            )
            '''
        )
    def CreateTableMembuatForum(self):
        self.cursor.execute(
            '''
            CREATE TABLE MembuatForum(
                forumID INTEGER NOT NULL,
                userID INTEGER NOT NULL,
                appID INTEGER NOT NULL,
                PRIMARY KEY (forumID, userID, appID),
                FOREIGN KEY (forumID) REFERENCES Forum(forumID) ON DELETE CASCADE,
                FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
                FOREIGN KEY (appID) REFERENCES Apps(appID) ON DELETE CASCADE
            )
            '''   
        )
    def CreateTablePost(self):
        self.cursor.execute(
            '''
            CREATE TABLE Post(
                postID INTEGER NOT NULL AUTO_INCREMENT,
                forumID INTEGER NOT NULL,
                userID INTEGER NOT NULL,
                konten_post VARCHAR(255) NOT NULL,
                waktu_pembuatan_post date NOT NULL,
                PRIMARY KEY(postID),
                FOREIGN KEY (forumID) REFERENCES Forum(forumID) ON DELETE CASCADE,
                FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE
            )
            '''
        )
    def CreateTableVote(self):
        self.cursor.execute(
            '''
            CREATE TABLE Vote(
                forumID INTEGER NOT NULL,
                userID INTEGER NOT NULL,
                jenis_vote ENUM("UPVOTE", "DOWNVOTE"),
                PRIMARY KEY (forumID, userID),
                FOREIGN KEY (forumID) REFERENCES Forum(forumID) ON DELETE CASCADE,
                FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE
            )
            '''
        )
    def CreateTableAward(self):
        self.cursor.execute(
            '''
            CREATE TABLE Award(
                awardID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
                gameID INTEGER,
                kategori VARCHAR(20) NOT NULL,
                FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE SET NULL
            )
            '''
        )
    def CreateTableGenre(self):
        self.cursor.execute(
            '''
            CREATE TABLE Genre(
                gameID INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                genre VARCHAR(20) NOT NULL,
                FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE CASCADE
            )
            '''
        )
    def InitiateAllTable(self):
        if(self.isDatabaseInitialized):
            print("Database has already been initialized")
            return
        self.CreateTableDeveloper()
        self.CreateTableApps()
        self.CreateTableUser()
        self.CreateTablePertemanan()
        self.CreateTableMemilikiAplikasi()
        self.CreateTableVideoGames()
        self.CreateTableSoundtrack()
        self.CreateTableLagu()
        self.CreateTableMenggunakanLagu()
        self.CreateTableAward()
        self.CreateTableGenre()
        self.CreateTableFollow()
        self.CreateTableForum()
        self.CreateTableMembuatForum()
        self.CreateTableVote()
        self.CreateTablePost()
        self.CreateTableDLC()
        self.CreateTableVideoGamesDLC()

        self.connection.commit()
        self.connection.close()
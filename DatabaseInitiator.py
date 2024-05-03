import mysql.connector;

class DatabaseInitiator:
    def __init__(self):
        self.connection = mysql.connector.connect(
            port = 49680,
            host = "localhost",
            user = "root",
            password = "",
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("SHOW DATABASES LIKE 'stim'")
        database_exists = bool(self.cursor.fetchall())

        # If the database doesn't exist, create it
        if not database_exists:
            self.cursor.execute("CREATE DATABASE stim")
                # Close the connection without specifying a database
        self.connection.close()

        # Reconnect to MySQL server and specify the 'stim' database
        self.connection = mysql.connector.connect(
            port=49680,
            host="localhost",
            user="root",
            password="",
            database="stim"
        )
        self.cursor = self.connection.cursor()

    def CreateTableApps(self):
        self.cursor.execute(
            '''
            CREATE TABLE Apps(
                appID INTEGER AUTO_INCREMENT PRIMARY KEY NOT NULL ,
                devID INTEGER NOT NULL,
                judul VARCHAR(50) NOT NULL,
                tanggal_peluncuran date,
                ukuran FLOAT,
                deskripsi VARCHAR(255),
                harga INTEGER DEFAULT 0,
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
                dlcID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
                gameID INTEGER NOT NULL,
                FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE CASCADE
            )
            '''        
        )

    def CreateTableDLCDetail(self):
        self.cursor.execute(
            '''
            CREATE TABLE DLCDetail(
                dlcID INTEGER NOT NULL,
                judul VARCHAR(50) NOT NULL,
                harga CHAR(10) NOT NULL DEFAULT '0',
                tanggal_peluncuran date,
                PRIMARY KEY(dlcID),
                FOREIGN KEY (dlcID) REFERENCES DLC(dlcID) ON DELETE CASCADE
            )
            '''
        )

    def CreateTableDeveloper(self):
        self.cursor.execute(
            '''
            CREATE TABLE Developer(
                devID INTEGER PRIMARY KEY AUTO_INCREMENT,
                email VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                nama_depan VARCHAR(255) NOT NULL, 
                nama_belakang VARCHAR(255) DEFAULT "",
                tanggal_lahir DATE,
                usia INTEGER
            )
            '''
        )

    def CreateTableUser(self):
        self.cursor.execute(
            '''
            CREATE TABLE User(
                userID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
                email VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                name_depan VARCHAR(255) NOT NULL, 
                nama_belakang VARCHAR(255) DEFAULT "",
                tanggal_lahir date,
                usia INTEGER,
                level INTEGER DEFAULT 0,
                balance FLOAT DEFAULT 0.0
            )
            '''
        )
    def CreateTableMemilikiAplikasi(self):
        self.cursor.execute(
            '''
            CREATE TABLE MemilikiAplikasi(
                userID INTEGER NOT NULL 
                appID INTEGER NOT NULL,
                total_waktu FLOAT,
                waktu_terakhir date,
                jumlah_achievement INTEGER DEFAULT 0,
                rating INTEGER CHECK(rating >= 0 and rating <= 5) DEFAULT 0,
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
                soundtrackID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
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
                developerID INTEGER NOT NULL,
                userID INTEGER NOT NULL,
                PRIMARY KEY (developerID, userID),
                FOREIGN KEY (developerID) REFERENCES Developer(developerID) ON DELETE CASCADE,
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
                waktu_pembuatan_vorum date NOT NULL,
                PRIMARY KEY(forumID)
                FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE SET NULL
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
                gameID INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
                genre VARCHAR(20) NOT NULL,
                FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE CASCADE
            )
            '''
        )
    def InitiateAllTable(self):
        self.CreateTableDeveloper()
        self.CreateTableApps()
        # self.CreateTablePertemanan()
        self.CreateTableMemilikiAplikasi()
        self.CreateTableVideoGames()
        self.CreateTableSoundtrack()
        self.CreateTableMenggunakanLagu()
        self.CreateTableLagu()
        self.CreateTableAward()
        self.CreateTableGenre()
        self.CreateTableFollow()
        self.CreateTableForum()
        self.CreateTableMembuatForum()
        self.CreateTableVote()
        self.CreateTablePost()
        self.CreateTableDLC()
        self.CreateTableDLCDetail()

        self.connection.commit()
        self.connection.close()

db = DatabaseInitiator()
db.InitiateAllTable()
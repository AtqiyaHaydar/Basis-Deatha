CREATE TABLE Apps(
    appID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    devID INTEGER NOT NULL,
    judul VARCHAR(50) NOT NULL,
    tanggal_peluncuran date,
    ukuran NUMBER,
    deskripsi VARCHAR(255),
    harga CHAR(10) NOT NULL DEFAULT '0',
    FOREIGN KEY (devID) REFERENCES Developer(devID) ON DELETE RESTRICT,
);

CREATE TABLE Developer(
    devID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name_depan VARCHAR(255) NOT NULL, 
    nama_belakang VARCHAR(255) DEFAULT "",
    tanggal_lahir date,
    usia INTEGER,
)

CREATE TABLE User(
    userID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name_depan VARCHAR(255) NOT NULL, 
    nama_belakang VARCHAR(255) DEFAULT "",
    tanggal_lahir date,
    usia INTEGER,
    level INTEGER DEFAULT 0,
    balance FLOAT DEFAULT 0.0,
)

CREATE TABLE MemilikiAplikasi(
    userID INTEGER NOT NULL 
    appID INTEGER NOT NULL,
    total_waktu FLOAT DEFAULT 0,
    waktu_terakhir date,
    jumlah_achievement INTEGER DEFAULT 0,
    rating INTEGER CHECK(rating >= 0 and rating <= 5) DEFAULT 0,
    PRIMARY KEY (userID, appID),
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (appID) REFERENCES Apps(appID) ON DELETE CASCADE,
)

CREATE TABLE SoundTrack(
    soundtrackID INTEGER PRIMARY KEY NOT NULL,
    durasi_total_lagu FLOAT DEFAULT 0 NOT NULL,
    FOREIGN KEY (soundtrackID) REFERENCES Apps(appID) ON DELETE CASCADE
)

CREATE TABLE VideoGames(
    gameID INTEGER PRIMARY KEY NOT NULL, 
    FOREIGN KEY (gameID) REFERENCES Apps(appID) ON DELETE CASCADE
)

CREATE TABLE MenggunakanLagu(
    soundtrackID INTEGER NOT NULL,
    laguID INTEGER NOT NULL,
    PRIMARY KEY (soundtrackID, laguID),
    FOREIGN KEY (soundtrackID) REFERENCES SoundTrack(soundtrackID) ON DELETE CASCADE,
    FOREIGN KEY (laguID) REFERENCES Lagu(laguID) ON DELETE CASCADE
)
Create TABLE Lagu(
    laguID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    judul_lagu VARCHAR(30) NOT NULL,
    durasi_lagu FLOAT DEFAULT 0 NOT NULL,
)

CREATE TABLE Follow(
    developerID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    PRIMARY KEY (developerID, userID),
    FOREIGN KEY (developerID) REFERENCES Developer(developerID) ON DELETE CASCADE,
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
)

CREATE TABLE Pertemanan(
    user1ID INTEGER NOT NULL,
    user2ID INTEGER NOT NULL,
    status_pertemanan ENUM("FRIENDS", "PENDING", "BLOCKED"),
    PRIMARY KEY (user1ID, user2ID),
    FOREIGN KEY (user1ID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (user2ID) REFERENCES User(userID) ON DELETE CASCADE,
)

CREATE TABLE Forum(
    forumID INTEGER NOT NULL AUTOINCREMENT,
    judul VARCHAR(255) NOT NULL,
    waktu_pembuatan_vorum date NOT NULL,
    PRIMARY KEY(forumID)
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE SET NULL,
)

CREATE TABLE MembuatForum(
    forumID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    appID INTEGER NOT NULL,
    PRIMARY KEY (forumID, userID, appID),
    FOREIGN KEY (forumID) REFERENCES Forum(forumID) ON DELETE CASCADE,
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (appID) REFERENCES Apps(appID) ON DELETE CASCADE,
)

CREATE TABLE Post(
    postID INTEGER NOT NULL AUTOINCREMENT,
    forumID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    konten_post VARCHAR(255) NOT NULL,
    waktu_pembuatan_post date NOT NULL,
    PRIMARY KEY(postID),
    FOREIGN KEY (forumID) REFERENCES Forum(forumID) ON DELETE CASCADE,
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,   
)

CREATE TABLE Vote(
    forumID INTEGER NOT NULL,
    userID INTEGER NOT NULL,
    jenis_vote ENUM("UPVOTE", "DOWNVOTE"),
    PRIMARY KEY (forumID, userID),
    FOREIGN KEY (forumID) REFERENCES Forum(forumID) ON DELETE CASCADE,
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
)

CREATE TABLE DLC(
    dlcID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    gameID INTEGER NOT NULL,
    FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE CASCADE,
)

CREATE TABLE DLCDetail(
    dlcID INTEGER NOT NULL,
    judul VARCHAR(50) NOT NULL,
    harga CHAR(10) NOT NULL DEFAULT '0',
    tanggal_peluncuran date,
    PRIMARY KEY(dlcID),
    FOREIGN KEY (dlcID) REFERENCES DLC(dlcID) ON DELETE CASCADE,
)

CREATE TABLE Award(
    awardID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    gameID INTEGER,
    kategori VARCHAR(20) NOT NULL,
    FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE SET NULL,
)

CREATE TABLE Genre(
    gameID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    genre VARCHAR(20) NOT NULL,
    FOREIGN KEY (gameID) REFERENCES VideoGames(gameID) ON DELETE CASCADE,
)
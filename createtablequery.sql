CREATE TABLE Apps (
    app_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    developer_id INTEGER NOT NULL,
    judul VARCHAR(50) NOT NULL,
    harga CHAR(10) NOT NULL DEFAULT '0',
    tanggal_peluncuran date,
    rating INTEGER CHECK (rating >= 0 AND rating <= 5) DEFAULT 0,
    ukuran FLOAT,
    deskripsi VARCHAR(255),
    FOREIGN KEY (developer_id) REFERENCES Developer(developer_id) ON DELETE RESTRICT,
);

CREATE TABLE Developer(
    developer_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name_depan VARCHAR(255) NOT NULL, 
    nama_belakang VARCHAR(255) DEFAULT "",
    tanggal_lahir date,
    usia INTEGER,
)

CREATE TABLE User(
    user_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name_depan VARCHAR(255) NOT NULL, 
    nama_belakang VARCHAR(255) DEFAULT "",
    tanggal_lahir date,
    usia INTEGER,
    level INTEGER,
    balance FLOAT DEFAULT 0.0,
)

CREATE TABLE MemilikiAplikasi(
    user_id INTEGER NOT NULL 
    app_id INTEGER NOT NULL,
    total_waktu FLOAT DEFAULT 0,
    waktu_terakhir date,
    jumlah_achievement INTEGER DEFAULT 0,
    rating INTEGER CHECK(rating >= 0 and rating <= 5) DEFAULT 0,
    PRIMARY KEY (user_id, app_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (app_id) REFERENCES Apps(app_id) ON DELETE CASCADE,
)

CREATE TABLE SoundTrack(
    soundtrack_id INTEGER PRIMARY KEY NOT NULL,
    durasi_total_lagu FLOAT DEFAULT 0 NOT NULL,
    FOREIGN KEY (soundtrack_id) REFERENCES Apps(app_id) ON DELETE CASCADE
)

CREATE TABLE VideoGames(
    game_id INTEGER PRIMARY KEY NOT NULL, 
    FOREIGN KEY (game_id) REFERENCES Apps(app_id) ON DELETE CASCADE
)

CREATE TABLE MenggunakanLagu(
    soundtrack_id INTEGER NOT NULL,
    lagu_id INTEGER NOT NULL,
    PRIMARY KEY (soundtrack_id, lagu_id),
    FOREIGN KEY (soundtrack_id) REFERENCES SoundTrack(soundtrack_id) ON DELETE CASCADE,
    FOREIGN KEY (lagu_id) REFERENCES Lagu(lagu_id) ON DELETE CASCADE
)
Create TABLE Lagu(
    lagu_id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
    judul_lagu VARCHAR(30) NOT NULL,
    durasi_lagu FLOAT DEFAULT 0 NOT NULL,
)

CREATE TABLE Follow(
    developer_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (developer_id, user_id),
    FOREIGN KEY (developer_id) REFERENCES Developer(developer_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
)

CREATE TABLE Pertemanan(
    user_id INTEGER NOT NULL,
    user_id2 INTEGER NOT NULL,
    status_pertemanan ENUM("FRIENDS", "PENDING", "BLOCKED"),
    PRIMARY KEY (user_id, user_id2),
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id2) REFERENCES User(user_id) ON DELETE CASCADE,
)
CREATE TABLE Forum(
    forum_id INTEGER NOT NULL AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    judul VARCHAR(255) NOT NULL,
    waktu_pembuatan_vorum date NOT NULL,
    PRIMARY KEY(forum_id)
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE SET NULL,
)
CREATE TABLE Post(
    post_id INTEGER NOT NULL AUTOINCREMENT,
    forum_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    judul VARCHAR(255) NOT NULL,
    waktu_pembuatan_post date NOT NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY (forum_id) REFERENCES Forum(forum_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,   
)

CREATE TABLE Vote(
    forum_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (forum_id, user_id),
    FOREIGN KEY (forum_id) REFERENCES Forum(forum_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
)

CREATE TABLE DLC(
    game_id INTEGER NOT NULL,
    judul VARCHAR(255) NOT NULL,
    harga CHAR(10) NOT NULL DEFAULT 0,
    tanggal_peluncuran date NOT NULL,
    PRIMARY KEY(game_id),
    FOREIGN KEY (game_id) REFERENCES VideoGames(game_id) ON DELETE CASCADE,
)

CREATE TABLE Award(
    game_id INTEGER,
    kategori VARCHAR(20) NOT NULL,
    PRIMARY KEY(game_id),
    FOREIGN KEY (game_id) REFERENCES VideoGames(game_id) ON DELETE SET NULL,
)

CREATE TABLE Genre(
    game_id INTEGER,
    genre VARCHAR(20) NOT NULL,
    PRIMARY KEY(game_id),
    FOREIGN KEY (game_id) REFERENCES VideoGames(game_id) ON DELETE CASCADE,
)
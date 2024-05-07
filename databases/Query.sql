-- Query sederhana yang setidaknya melibatkan 3 buah relasi
SELECT CONCAT(User.nama_depan, ' ', User.nama_belakang) AS nama_lengkap, Forum.judul, Post.konten_post
    FROM User
    JOIN Post ON User.userID = Post.userID
    JOIN Forum ON Post.forumID = Forum.forumID;


-- Query dengan set operation yang setidaknya melibatkan 3 buah relasi
SELECT CONCAT(nama_depan, ' ', nama_belakang) AS nama_lengkap
    FROM User
    WHERE userID NOT IN (
        SELECT userID FROM Post
        UNION
        SELECT userID FROM Forum
        UNION
        SELECT userID FROM MemilikiAplikasi
    );


-- Query dengan agregasi yang setidaknya melibatkan setidaknya 4 relasi dengan group by dan having.
Melibatkan setidaknya 4 relasi dengan group by dan having.
SELECT concat(Developer.nama_depan,' ',Developer.nama_belakang) as nama_pengembang, COUNT(Apps.appID) AS jumlah_aplikasi
    FROM Developer
    JOIN Apps ON Developer.devID = Apps.devID
    JOIN (
         SELECT VideoGames.gameID, COUNT(*) AS jumlah_dlc
         FROM VideoGames
         JOIN DLC ON VideoGames.gameID = DLC.gameID
         GROUP BY VideoGames.gameID
         HAVING COUNT(*) >= 3
    ) AS AppsWithMin3DLC ON Apps.appID = AppsWithMin3DLC.gameID
    GROUP BY Developer.devID;


-- Query dengan SubQuery yang melibatkan setidaknya 3 relasi pada subquery dan 2 relasi pada query utama
SELECT DISTINCT CONCAT(d.nama_depan, ' ', d.nama_belakang) AS Developer_Name
FROM apps a
JOIN developer d ON a.devID = d.devID
JOIN forum f ON a.appID = f.appID
WHERE a.appID IN (
    SELECT ma.appID
    FROM memilikiaplikasi ma
    JOIN user u ON ma.userID = u.userID
    JOIN pertemanan p ON u.userID = p.user1ID
    WHERE p.status_pertemanan = 'FRIENDS' AND u.level > 5
);


-- Query kompleks yang melibatkan komponen query dengan agregasi dan set operation
SELECT *
FROM (
    SELECT a.appID, a.judul, SUM(ma.total_waktu) AS total_waktu_penggunaan
    FROM apps a
    JOIN memilikiaplikasi ma ON a.appID = ma.appID
    JOIN user u ON ma.userID = u.userID
    WHERE u.level > 5
    GROUP BY a.appID, a.judul
    HAVING total_waktu_penggunaan > (SELECT AVG(total_waktu) FROM memilikiaplikasi)
    UNION
    SELECT a.appID, a.judul, NULL AS total_waktu_penggunaan
    FROM apps a
    WHERE a.harga < (SELECT AVG(harga) FROM apps)
) AS combined_results
HAVING total_waktu_penggunaan IS NOT NULL
ORDER BY total_waktu_penggunaan DESC;
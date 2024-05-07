# Basis DEATH-A: Relational Diagram Implementation to SQL Database

> 🌐 Milestone 2 of Database Major Assignment

🎓 **Project Background:**
I created the Relational Diagram Implementation to SQL Database as part of my Database second milestone assignment during my fourth semester in the Computer Science program at ITB.

## 🪪 Contributors
| Name |
|---|
|Kartini Copa|
| Aland Mulia Pratama |
|Farhan Raditya Aji|
|Muhammad Davis Adhipramana|
|Atqiya Haydar Luqman|


## 📝 Description
All processes, including the creation of database tables and seeding the database, are conducted using Python. The database creation process begins with initializing a connection to the MySQL server and checking the availability of a specific database. If the database does not exist, a new one is created using the SQL statement CREATE DATABASE, followed by establishing a specific connection to the designated database. Subsequently, the program initializes tables with the necessary columns and relational constraints using SQL CREATE TABLE statements. After creating all tables, the transaction is committed to save all changes to the database. The database seeding process commences with initializing the Faker library and reconnecting to the database. The program retrieves all existing IDs from specific tables (e.g., user IDs, application IDs, developer IDs, etc.) to establish connections between different entities during seeding. Fake data is generated realistically using Faker, such as names, addresses, dates of birth, etc., which are then associated and inserted into the database using SQL INSERT statements.

## 📁 Project Structure
```bash
Basis-Deatha
├── Milestone2_SLS_Fresh Milk with Grass Jelly.zip
├── README.md
├── databases
│   ├── Milestone2_SLS_Fresh Milk with Grass Jelly.sql
│   └── Query.sql
├── doc
│   └── Milestone2_SLS_Fresh Milk with Grass Jelly.pdf
├── requirement.txt
└── src
    ├── DatabaseInitiator.py
    ├── Seeding.py
    ├── __pycache__
    │   ├── DatabaseInitiator.cpython-311.pyc
    │   ├── Seeding.cpython-311.pyc
    │   └── menu.cpython-311.pyc
    ├── createtablequery.sql
    ├── main.py
    ├── menu.py
    └── relation
        ├── __pycache__
        │   ├── apps.cpython-311.pyc
        │   ├── award.cpython-311.pyc
        │   ├── developer.cpython-311.pyc
        │   ├── dlc.cpython-311.pyc
        │   ├── follow.cpython-311.pyc
        │   ├── forum.cpython-311.pyc
        │   ├── genre.cpython-311.pyc
        │   ├── lagu.cpython-311.pyc
        │   ├── membuatforum.cpython-311.pyc
        │   ├── memilikiaplikasi.cpython-311.pyc
        │   ├── menggunakanlagu.cpython-311.pyc
        │   ├── pertemanan.cpython-311.pyc
        │   ├── post.cpython-311.pyc
        │   ├── soundtrack.cpython-311.pyc
        │   ├── user.cpython-311.pyc
        │   ├── videogames.cpython-311.pyc
        │   └── vote.cpython-311.pyc
        ├── apps.py
        ├── award.py
        ├── developer.py
        ├── dlc.py
        ├── follow.py
        ├── forum.py
        ├── genre.py
        ├── lagu.py
        ├── membuatforum.py
        ├── memilikiaplikasi.py
        ├── menggunakanlagu.py
        ├── pertemanan.py
        ├── post.py
        ├── soundtrack.py
        ├── user.py
        ├── videogames.py
        ├── videogamesdlc.py
        └── vote.py
```
## Requirement
 • Python3 (https://www.python.org/downloads/)
 • MariaDB v10.11 or higher (https://mariadb.org/download/)

## How to Run
1. Change the terminal directory to `Basis-Deatha`.
2. Execute `pip install -r requirement.txt`.
3. After requirements are succesfully installed, change the directory to `Basis-Deatha/src`.
4. Open `main.py` file with your IDE (VSCode/PyCharm) and edit the port, host, user, and password that suitable with the server of your MariaDB.
5. You can identify your port by executing query `SHOW GLOBAL VARIABLES LIKE 'port';` on your MariaDB server.
5. Run `python3 main.py` in the terminal, there will be 18 menu in the program if the port, host, user, and password match.
6. For the easiest way, you can input `All` and input the num to create as you desire with integer format.
7. Wait for a second and the Stim database will be created on your SQL Server.

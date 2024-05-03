
# from faker import Faker 
# import mysql.connector

db = mysql.connector.connect(
    port = 49680,
    host = "localhost",
    user = "root",
    password = "",
    database = "test"
)

# cursor = db.cursor()    
# fake = Faker()
# def seed_database(num_records):
#     for _ in range(num_records):
#         name = fake.name()
#         email = fake.email()
#         sql = f"INSERT INTO Apps (name, email) VALUES (%s, %s)"
#         val = (name, email)
#         cursor.execute(sql, val)

#         db.commit()

# seed_database()
# print("Seeding success")
# cursor.close()
# db.close()

if __name__ == "main":
    pass
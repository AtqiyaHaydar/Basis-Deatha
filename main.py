from faker import Faker 
import mysql.connector
from relation.developer import Developer
db = mysql.connector.connect(
    port = 49680,
    host = "localhost",
    user = "root",
    password = "",
    database = "stim"
)
num_records = 5
developer = Developer(db)
developer.seeding(num_records)
print("SUCCESS ANJING")

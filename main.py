import mysql.connector
from menu import menu

db = mysql.connector.connect(
    port = 49680,
    host = "localhost",
    user = "root",
    password = "",
    database = "stim"
)
num_records = 50
# Developer
Menu = menu(db)

Menu.showMenu()
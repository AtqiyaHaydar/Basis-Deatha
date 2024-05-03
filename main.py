import mysql.connector
from menu import menu
from DatabaseInitiator import DatabaseInitiator


# Please Change this to your exact machine 
connection = mysql.connector.connect(
            port = 49680,
            host = "localhost",
            user = "root",
            password = "",
)

DatabaseInit = DatabaseInitiator(connection)
DatabaseInit.InitiateAllTable()

# Get Stim Database
db = DatabaseInit.getStimDatabase()

# Developer
Menu = menu(db)

Menu.showMenu()
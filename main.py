from menu import menu
from DatabaseInitiator import DatabaseInitiator

# Check your port by Input
# SHOW GLOBAL VARIABLES LIKE 'port'
port = 3306
host = "localhost"
user = "root"
password = ""


DatabaseInit = DatabaseInitiator(port, host, user, password)
DatabaseInit.InitiateAllTable()

# Get Stim Database
db = DatabaseInit.getStimDatabase()

# Developer
Menu = menu(db)

Menu.showMenu()
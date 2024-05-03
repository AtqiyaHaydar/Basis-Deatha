from faker import Faker
from datetime import datetime
import random

class Seeding():
    def __init__(self, connection):
        self.fake = Faker()
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.db = self.connection
        self.developer_ids = []
        self.random = random
    
    def seeding(self, num_records):
        pass

    # Menghitung Umur
    def calculate_age(self,date_of_birth):
        today = datetime.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age

    def get_all_user_id(self):
        self.cursor.execute("SELECT userID FROM USER")
        result = self.cursor.fetchall()
        new_user_ids = []

        for row in result:
            new_user_ids.append(row[0])
        
        return new_user_ids

    def get_all_dev_id(self):
        self.cursor.execute("SELECT devID FROM DEVELOPER")
        result = self.cursor.fetchall()
        new_dev_ids = []

        for row in result:
            new_dev_ids.append(row[0])
        
        return new_dev_ids
        
    def get_all_app_id(self):
        self.cursor.execute("SELECT appID FROM APPS")
        result = self.cursor.fetchall()
        new_app_ids = []

        for row in result:
            new_app_ids.append(row[0])
        
        return new_app_ids

    def get_all_soundtrack_id(self):
        self.cursor.execute("SELECT soundtrackID FROM SOUNDTRACK")
        result = self.cursor.fetchall()
        new_soundtrack_id = []

        for row in result:
            new_soundtrack_id.append(row[0])
        
        return new_soundtrack_id

    def get_all_song_id(self):
        self.cursor.execute("SELECT laguID FROM LAGU")
        result = self.cursor.fetchall()
        new_song_id = []

        for row in result:
            new_song_id.append(row[0])
        
        return new_song_id

    def get_all_videogames_id(self):
        self.cursor.execute("SELECT gameID FROM VIDEOGAMES")
        result = self.cursor.fetchall()
        new_videogames_id = []

        for row in result:
            new_videogames_id.append(row[0])
        
        return new_videogames_id

    def get_all_dlc_id(self):
        self.cursor.execute("SELECT dlcID FROM DLC")
        result = self.cursor.fetchall()
        new_dlc_id = []

        for row in result:
            new_dlc_id.append(row[0])
        
        return new_dlc_id

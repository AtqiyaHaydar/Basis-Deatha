from faker import Faker
import mysql.connector
from datetime import datetime
import random

class Seeding():
    def __init__(self, connection):
        self.fake = Faker()
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.db = self.connection
        self.user_ids = []
        self.developer_ids = []
    def seeding(self, num_records):
        pass

    # Generate Username
    def generate_username(first_name, last_name):
        return f"{first_name.lower()}.{last_name.lower()}"

    # Menghitung Umur
    def calculate_age(date_of_birth):
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
        
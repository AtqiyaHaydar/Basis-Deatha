from faker import Faker
from datetime import datetime
import mysql.connector

class Seeding():
    def __init__(self, connection):
        self.fake = Faker()
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.db = self.connection
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
        return fake.random_number(digits=None, fix_len=False)
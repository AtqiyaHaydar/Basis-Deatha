from faker import Faker
import mysql.connector
class Seeding():
    def __init__(self, connection):
        self.faker = Faker()
        self.connection = connection
        self.cursor = self.connection.cursor()
    def seeding(self):
        pass